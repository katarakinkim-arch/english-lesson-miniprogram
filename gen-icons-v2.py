#!/usr/bin/env python3
"""
Generate high-quality tabBar icons for the English Lesson Mini Program.
Style: Modern line-art / minimal outline — clean, professional, anti-aliased.
Size: 81x81px (WeChat requirement), transparent background.
Normal: #999999, Selected: #1a365d (brand deep blue)
"""

from PIL import Image, ImageDraw
import math, os

SIZE = 81
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', 'tabbar')
os.makedirs(OUT_DIR, exist_ok=True)

# Colors (RGBA)
NORMAL = (153, 153, 153, 255)       # #999999
ACTIVE = (26, 54, 93, 255)          # #1a365d

def new_canvas():
    """Create transparent canvas."""
    return Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))

def draw_round_cap_line(draw, p1, p2, width, color):
    """Draw a line with round caps using thick polygon approximation."""
    # PIL's line doesn't do round caps well; use circle endpoints + rectangle middle
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    length = math.hypot(dx, dy) or 1.0
    ux, uy = dx / length, dy / length  # unit vector
    px, py = -uy, ux                   # perpendicular

    hw = width / 2.0
    # Rectangle body
    pts = [
        (p1[0] + px * hw, p1[1] + py * hw),
        (p2[0] + px * hw, p2[1] + py * hw),
        (p2[0] - px * hw, p2[1] - py * hw),
        (p1[0] - px * hw, p1[1] - py * hw),
    ]
    draw.polygon(pts, fill=color)
    # Round caps
    draw.ellipse([p1[0]-hw, p1[1]-hw, p1[0]+hw, p1[1]+hw], fill=color)
    draw.ellipse([p2[0]-hw, p2[1]-hw, p2[0]+hw, p2[1]+hw], fill=color)

def draw_thick_arc(draw, cx, cy, r, start_deg, end_deg, width, color, nseg=36):
    """Draw an arc as thick line segments."""
    steps = max(int(abs(end_deg - start_deg) / 360 * nseg), 4)
    pts = []
    for i in range(steps + 1):
        deg = math.radians(start_deg + (end_deg - start_deg) * i / steps)
        pts.append((cx + r * math.cos(deg), cy + r * math.sin(deg)))
    for i in range(len(pts) - 1):
        draw_round_cap_line(draw, pts[i], pts[i+1], width, color)


# ====== ICON 1: HOME (教案库) — Modern house shape with subtle book hint ======
def draw_home(color):
    img = new_canvas()
    d = ImageDraw.Draw(img)

    sw = 4.5  # stroke width (in source coords, will scale up)
    c = SIZE // 2

    # Roof: triangle pointing up
    roof_top = (c, 14)
    roof_left = (14, 38)
    roof_right = (SIZE - 14, 38)

    # House body: rectangle below roof
    wall_tl = (20, 36)
    wall_br = (SIZE - 20, SIZE - 10)

    # Door: centered at bottom
    door_w = 16
    door_h = 18
    door_l = (c - door_w // 2, SIZE - 10 - door_h)
    door_r = (c + door_w // 2, SIZE - 10)

    # Draw roof lines
    d.line([roof_top, roof_left], fill=color, width=int(sw) + 1)
    d.line([roof_top, roof_right], fill=color, width=int(sw) + 1)

    # Draw walls (open bottom = no base line, just sides)
    d.line([wall_tl, (wall_tl[0], wall_br[1])], fill=color, width=int(sw) + 1)
    d.line([(wall_br[0], wall_tl[1]), wall_br], fill=color, width=int(sw) + 1)

    # Draw door (U-shape: left, bottom, right)
    d.line([door_l, (door_l[0], door_r[1])], fill=color, width=int(sw))
    d.line([(door_r[0], door_l[1]), door_r], fill=color, width=int(sw))
    d.line([door_l, (door_r[0], door_l[1])], fill=color, width=int(sw))

    # Small dot on door (knob)
    knob_r = 2.5
    d.ellipse([
        door_r[0] - knob_r - 4, c + 2 - knob_r,
        door_r[0] - knob_r - 4 + knob_r * 2, c + 2 + knob_r * 2
    ], fill=color)

    return img


# ====== ICON 2: STAR (收藏) — Clean 5-point star, balanced proportions ======
def draw_star(color):
    img = new_canvas()
    d = ImageDraw.Draw(img)

    c = SIZE // 2
    outer_r = 30   # outer radius of star points
    inner_r = 12   # inner radius (between points)
    sw = 5         # stroke width

    # Generate 5-point star vertices
    points = []
    for i in range(10):  # 5 outer + 5 inner alternating
        angle = math.radians(-90 + i * 36)  # start from top (-90°)
        r = outer_r if i % 2 == 0 else inner_r
        x = c + r * math.cos(angle)
        y = c + r * math.sin(angle)
        points.append((x, y))

    # Draw star outline (connect all 10 points)
    for i in range(10):
        p1 = points[i]
        p2 = points[(i + 1) % 10]
        d.line([p1, p2], fill=color, width=sw)

    return img


# ====== ICON 3: PERSON (我的) — Clean head-and-shoulders silhouette ======
def draw_person(color):
    img = new_canvas()
    d = ImageDraw.Draw(img)

    sw = 5  # stroke width

    # Head: circle near top-center
    head_cx = SIZE // 2
    head_cy = 24
    head_r = 13

    # Body: shoulders arc (wider than head)
    shoulder_cy = SIZE - 6
    shoulder_width = 28

    # Draw head circle
    d.ellipse([
        head_cx - head_r, head_cy - head_r,
        head_cx + head_r, head_cy + head_r
    ], outline=color, width=sw)

    # Draw body: arc from left shoulder to right shoulder
    # Using a wide arc that forms the shoulder curve
    l_shoulder = (head_cx - shoulder_width, shoulder_cy - 8)
    r_shoulder = (head_cx + shoulder_width, shoulder_cy - 8)
    bottom_center = (head_cx, shoulder_cy + 4)

    # Shoulders: two curves meeting at center bottom
    d.arc(
        [l_shoulder[0] - 8, l_shoulder[1] - 12, bottom_center[0] + 8, bottom_center[1] + 8],
        start=180, end=360,
        fill=color, width=sw
    )
    d.arc(
        [bottom_center[0] - 8, bottom_center[1] - 8, r_shoulder[0] + 8, r_shoulder[1] + 12],
        start=180, end=360,
        fill=color, width=sw
    )

    return img


# ====== GENERATE ALL 6 ICONS ======
icons = {
    'home':      ('home.png',       'home-active.png',       draw_home),
    'star':      ('star.png',       'star-active.png',       draw_star),
    'person':    ('person.png',     'person-active.png',     draw_person),
}

for name, (normal_file, active_file, draw_fn) in icons.items():
    normal_img = draw_fn(NORMAL)
    active_img = draw_fn(ACTIVE)

    normal_path = os.path.join(OUT_DIR, normal_file)
    active_path = os.path.join(OUT_DIR, active_file)

    normal_img.save(normal_path)
    active_img.save(active_path)

    print(f'  {name}: {normal_file} ({normal_img.size[0]}x{normal_img.size[1]}, {os.path.getsize(normal_path)}B)')
    print(f'  {name}: {active_file} ({active_img.size[0]}x{active_img.size[1]}, {os.path.getsize(active_path)}B)')

print(f'\nAll icons saved to: {OUT_DIR}')
