import math
import random

def generate_portrait_dots():
    dots = []
    # Seed for reproducibility
    random.seed(42)
    
    # Define face/head/shoulders shape boundaries relative to center (x=160, y=210)
    # Head circle / oval: center (160, 150), rx=55, ry=70
    # Hair / top: rx=58, ry=50
    # Shoulders / torso: center (160, 290), rx=110, ry=65
    
    # Head & Face density
    for _ in range(2200):
        # Sample points within head/hair/face
        angle = random.uniform(0, 2 * math.pi)
        r = math.sqrt(random.uniform(0, 1))
        
        # Determine if head, hair, neck or shoulder
        part = random.choices(['head', 'hair', 'glasses', 'shoulders', 'neck'], weights=[0.35, 0.25, 0.1, 0.25, 0.05])[0]
        
        if part == 'head':
            px = 160 + r * 50 * math.cos(angle)
            py = 155 + r * 65 * math.sin(angle)
        elif part == 'hair':
            px = 160 + r * 56 * math.cos(angle)
            py = 135 + r * 45 * math.sin(angle)
        elif part == 'glasses':
            # Cyber glasses frame across eyes (y ~ 145)
            px = random.uniform(125, 195)
            py = random.uniform(142, 152)
        elif part == 'neck':
            px = 160 + random.uniform(-22, 22)
            py = random.uniform(215, 240)
        else: # shoulders
            px = 160 + r * 115 * math.cos(angle)
            py = 285 + r * 55 * math.sin(angle)
            if py < 235:
                continue
        
        # Add slight jitter
        px += random.gauss(0, 1.2)
        py += random.gauss(0, 1.2)
        
        dots.append((round(px, 1), round(py, 1)))

    return dots

def build_animated_svg(is_dark=True):
    dots = generate_portrait_dots()
    
    # Colors
    if is_dark:
        bg_main = "#0A101F"
        bg_card = "#0C1426"
        grid_stroke = "#1E293B"
        dot_base = "#38BDF8"
        dot_alt = "#A78BFA"
        dot_highlight = "#22D3EE"
        text_primary = "#F8FAFC"
        text_sub = "#94A3B8"
        text_accent = "#22D3EE"
        text_purple = "#A78BFA"
        text_green = "#10B981"
        header_bg = "#060A14"
        leader_color = "#334155"
        border_color = "#1E293B"
    else:
        bg_main = "#FFFFFF"
        bg_card = "#F8FAFC"
        grid_stroke = "#E2E8F0"
        dot_base = "#0284C7"
        dot_alt = "#7C3AED"
        dot_highlight = "#0891B2"
        text_primary = "#0F172A"
        text_sub = "#475569"
        text_accent = "#0891B2"
        text_purple = "#7C3AED"
        text_green = "#059669"
        header_bg = "#E2E8F0"
        leader_color = "#CBD5E1"
        border_color = "#CBD5E1"

    # Group dots into 25 animated SMIL groups for flickering / shimmering portrait effect
    groups_xml = []
    num_groups = 30
    dots_per_group = len(dots) // num_groups
    
    random.seed(123)
    random.shuffle(dots)
    
    for i in range(num_groups):
        grp_dots = dots[i*dots_per_group : (i+1)*dots_per_group]
        dur = round(random.uniform(2.5, 4.5), 2)
        begin_delay = round(random.uniform(0, 2.0), 2)
        dx = round(random.uniform(-3, 3), 1)
        dy = round(random.uniform(-3, 3), 1)
        
        path_data = " ".join([f"M{d[0]} {d[1]}h1.5v1.5h-1.5z" for d in grp_dots])
        color = dot_base if i % 3 == 0 else (dot_alt if i % 3 == 1 else dot_highlight)
        
        grp_str = f'''    <g fill="{color}">
      <animate attributeName="opacity" values="0.3;1;0.5;0.9;0.3" dur="{dur}s" begin="{begin_delay}s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="translate" values="0 0; {dx} {dy}; 0 0" dur="{dur*1.5:.2f}s" begin="{begin_delay}s" repeatCount="indefinite"/>
      <path d="{path_data}"/>
    </g>'''
        groups_xml.append(grp_str)

    # Floating travelling swarm dots moving towards logos (morph effect)
    travellers_xml = []
    for _ in range(120):
        sx = random.uniform(100, 220)
        sy = random.uniform(120, 280)
        tx = random.uniform(300, 360)
        ty = random.uniform(100, 300)
        dur = round(random.uniform(3.0, 6.0), 2)
        delay = round(random.uniform(0, 4.0), 2)
        color = random.choice([dot_base, dot_alt, dot_highlight])
        
        t_str = f'''    <circle cx="{sx}" cy="{sy}" r="1.5" fill="{color}" opacity="0">
      <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.2;0.8;1" dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/>
      <animate attributeName="cx" values="{sx};{tx};{sx}" dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="{sy};{ty};{sy}" dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/>
    </circle>'''
        travellers_xml.append(t_str)

    portrait_svg_block = "\n".join(groups_xml)
    travellers_svg_block = "\n".join(travellers_xml)

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="610" viewBox="0 0 1180 610" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace" role="img" aria-label="Safir Akhtar — profile.sh --live">
  <defs>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{dot_alt}"><animate attributeName="stop-color" values="{dot_alt};{dot_highlight};{text_green};{dot_alt}" dur="10s" repeatCount="indefinite"/></stop>
      <stop offset="0.5" stop-color="{dot_highlight}"><animate attributeName="stop-color" values="{dot_highlight};{text_green};{dot_alt};{dot_highlight}" dur="10s" repeatCount="indefinite"/></stop>
      <stop offset="1" stop-color="{text_green}"><animate attributeName="stop-color" values="{text_green};{dot_alt};{dot_highlight};{text_green}" dur="10s" repeatCount="indefinite"/></stop>
    </linearGradient>

    <pattern id="gridPattern" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{grid_stroke}" stroke-width="0.5" stroke-opacity="0.3"/>
      <circle cx="40" cy="0" r="1.5" fill="{dot_highlight}" fill-opacity="0.3"/>
    </pattern>
  </defs>

  <!-- Background -->
  <rect width="1180" height="610" rx="16" fill="{bg_card}" stroke="{border_color}" stroke-width="2"/>
  <rect width="1180" height="610" rx="16" fill="url(#gridPattern)"/>

  <!-- Top Terminal Header Bar -->
  <path d="M 0 16 C 0 7.163 7.163 0 16 0 L 1164 0 C 1172.837 0 1180 7.163 1180 16 L 1180 48 L 0 48 Z" fill="{header_bg}"/>
  <circle cx="28" cy="24" r="6.5" fill="#EF4444"/>
  <circle cx="48" cy="24" r="6.5" fill="#F59E0B"/>
  <circle cx="68" cy="24" r="6.5" fill="#10B981"/>
  <text x="590" y="29" text-anchor="middle" fill="{text_sub}" font-size="14" font-weight="600">safir-akhtar ~ profile.sh --live</text>
  <line x1="0" y1="48" x2="1180" y2="48" stroke="{border_color}" stroke-width="1"/>

  <!-- LEFT SIDE: Animated Dot Matrix Dithered Portrait -->
  <g transform="translate(10, 45)">
    <!-- Animated Dot Groups -->
{portrait_svg_block}
    <!-- Swarm Travellers -->
{travellers_svg_block}

    <!-- Name & Subtitle overlay under portrait -->
    <text x="160" y="375" text-anchor="middle" fill="url(#accent)" font-size="32" font-weight="800" font-family="'Segoe UI', sans-serif" letter-spacing="0.5">Safir Akhtar</text>
    <text x="160" y="400" text-anchor="middle" fill="{text_sub}" font-size="14" font-weight="500" font-family="'Segoe UI', sans-serif">17 y/o Full-Stack Dev &amp; Creative Technologist</text>
    <text x="160" y="425" text-anchor="middle" fill="{text_accent}" font-size="15" font-weight="700" font-family="monospace">&lt;/&gt; Developer &amp; AI Automation Specialist</text>

    <!-- Floating Morph Target Badges -->
    <g transform="translate(370, 110)">
      <rect x="0" y="0" width="115" height="32" rx="16" fill="{header_bg}" stroke="{dot_highlight}" stroke-width="1"/>
      <text x="57.5" y="21" text-anchor="middle" fill="{dot_highlight}" font-size="12" font-weight="700">&lt;/&gt; Code</text>

      <rect x="0" y="48" width="115" height="32" rx="16" fill="{header_bg}" stroke="{dot_alt}" stroke-width="1"/>
      <text x="57.5" y="69" text-anchor="middle" fill="{dot_alt}" font-size="12" font-weight="700">Python/Go</text>

      <rect x="0" y="96" width="115" height="32" rx="16" fill="{header_bg}" stroke="{text_green}" stroke-width="1"/>
      <text x="57.5" y="117" text-anchor="middle" fill="{text_green}" font-size="12" font-weight="700">AI Prompt</text>

      <rect x="0" y="144" width="115" height="32" rx="16" fill="{header_bg}" stroke="{dot_highlight}" stroke-width="1"/>
      <text x="57.5" y="165" text-anchor="middle" fill="{dot_highlight}" font-size="12" font-weight="700">UI/UX &amp; 3D</text>

      <rect x="0" y="192" width="115" height="32" rx="16" fill="{header_bg}" stroke="{dot_alt}" stroke-width="1"/>
      <text x="57.5" y="213" text-anchor="middle" fill="{dot_alt}" font-size="12" font-weight="700">AE &amp; PR Video</text>
    </g>

    <!-- Live Status Box -->
    <g transform="translate(30, 445)">
      <rect width="455" height="75" rx="14" fill="{header_bg}" stroke="{border_color}" stroke-width="1.5"/>
      <circle cx="28" cy="37.5" r="6" fill="{text_green}">
        <animate attributeName="opacity" values="1;0.2;1" dur="2s" repeatCount="indefinite"/>
      </circle>
      <circle cx="28" cy="37.5" r="11" fill="none" stroke="{text_green}" stroke-width="1.5" stroke-opacity="0.5">
        <animate attributeName="r" values="6;14;6" dur="2s" repeatCount="indefinite"/>
        <animate attributeName="stroke-opacity" values="0.8;0;0.8" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text x="50" y="33" fill="{text_primary}" font-size="14" font-weight="700" font-family="'Segoe UI', sans-serif">STATUS: <tspan fill="{text_green}">BUILDING &amp; AUTOMATING</tspan></text>
      <text x="50" y="53" fill="{text_sub}" font-size="12" font-family="'Segoe UI', sans-serif">Web Systems · AI Prompting · Video Editing &amp; 3D</text>
    </g>
  </g>

  <!-- RIGHT SIDE: Terminal Info Panel (Spec from Guide) -->
  <g transform="translate(630, 75)">
    <rect width="490" height="480" rx="16" fill="{header_bg}" stroke="{border_color}" stroke-width="1.5"/>
    
    <!-- Info Panel Bar -->
    <path d="M 0 16 C 0 7.163 7.163 0 16 0 L 474 0 C 482.837 0 490 7.163 490 16 L 490 38 L 0 38 Z" fill="{header_bg}"/>
    <text x="245" y="24" text-anchor="middle" fill="{text_sub}" font-size="13" font-weight="600">user-profile.json</text>
    <line x1="0" y1="38" x2="490" y2="38" stroke="{border_color}" stroke-width="1"/>

    <!-- Terminal Spec Rows -->
    <g transform="translate(25, 40)" font-size="13.5">
      <text y="35" fill="{text_purple}" font-weight="700">Subject</text>
      <text x="110" y="35" fill="{leader_color}">......................................</text>
      <text x="440" y="35" text-anchor="end" fill="{text_primary}">Safir Akhtar</text>

      <text y="72" fill="{text_purple}" font-weight="700">Age</text>
      <text x="110" y="72" fill="{leader_color}">......................................</text>
      <text x="440" y="72" text-anchor="end" fill="{text_accent}">17 Years Old</text>

      <text y="109" fill="{text_purple}" font-weight="700">Handle</text>
      <text x="110" y="109" fill="{leader_color}">......................................</text>
      <text x="440" y="109" text-anchor="end" fill="#F472B6">@Nystic-Shadow</text>

      <text y="146" fill="{text_purple}" font-weight="700">Dev.Sign</text>
      <text x="110" y="146" fill="{leader_color}">......................................</text>
      <text x="440" y="146" text-anchor="end" fill="{text_green}">&lt;/&gt; Full-Stack &amp; Creative</text>

      <text y="183" fill="{text_purple}" font-weight="700">Core.Lang</text>
      <text x="110" y="183" fill="{leader_color}">......................................</text>
      <text x="440" y="183" text-anchor="end" fill="{dot_base}">Python · Node.js · Go</text>

      <text y="220" fill="{text_purple}" font-weight="700">Web.Dev</text>
      <text x="110" y="220" fill="{leader_color}">......................................</text>
      <text x="440" y="220" text-anchor="end" fill="#60A5FA">HTML5 · CSS3 · JavaScript</text>

      <text y="257" fill="{text_purple}" font-weight="700">UI/UX.Tools</text>
      <text x="110" y="257" fill="{leader_color}">......................................</text>
      <text x="440" y="257" text-anchor="end" fill="#F0ABFC">Figma · Adobe XD · Canva</text>

      <text y="294" fill="{text_purple}" font-weight="700">Graphic.Tools</text>
      <text x="110" y="294" fill="{leader_color}">......................................</text>
      <text x="440" y="294" text-anchor="end" fill="{text_sub}">Photoshop · Illustrator · CorelDRAW</text>

      <text y="331" fill="{text_purple}" font-weight="700">Video.Tools</text>
      <text x="110" y="331" fill="{leader_color}">......................................</text>
      <text x="440" y="331" text-anchor="end" fill="#FB7185">Premiere Pro · After Effects</text>

      <text y="368" fill="{text_purple}" font-weight="700">Dev.Tools</text>
      <text x="110" y="368" fill="{leader_color}">......................................</text>
      <text x="440" y="368" text-anchor="end" fill="{text_sub}">VS Code · Git</text>

      <text y="405" fill="{text_purple}" font-weight="700">AI.Skill</text>
      <text x="110" y="405" fill="{leader_color}">......................................</text>
      <text x="440" y="405" text-anchor="end" fill="{text_green}">Prompt Engineering &amp; Automation</text>
    </g>
  </g>
</svg>'''
    return svg_content

with open(r'C:\Users\SAZUZ\Nystic-Shadow\dark.svg', 'w', encoding='utf-8') as f:
    f.write(build_animated_svg(is_dark=True))

with open(r'C:\Users\SAZUZ\Nystic-Shadow\light.svg', 'w', encoding='utf-8') as f:
    f.write(build_animated_svg(is_dark=False))

print("Both animated dot matrix avatar SVGs generated successfully!")
