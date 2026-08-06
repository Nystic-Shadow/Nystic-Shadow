import math
import random

def build_svg(is_dark=True):
    if is_dark:
        bg_card = "#070B16"
        bg_panel = "#0B132B"
        grid_stroke = "#1E293B"
        border_color = "#1E293B"
        text_main = "#F8FAFC"
        text_sub = "#94A3B8"
        accent_cyan = "#22D3EE"
        accent_purple = "#A78BFA"
        accent_pink = "#F472B6"
        accent_green = "#10B981"
        header_bg = "#040711"
        leader_color = "#334155"
    else:
        bg_card = "#FFFFFF"
        bg_panel = "#F8FAFC"
        grid_stroke = "#E2E8F0"
        border_color = "#CBD5E1"
        text_main = "#0F172A"
        text_sub = "#475569"
        accent_cyan = "#0891B2"
        accent_purple = "#7C3AED"
        accent_pink = "#BE123C"
        accent_green = "#059669"
        header_bg = "#E2E8F0"
        leader_color = "#CBD5E1"

    # Build clean dot matrix avatar contour (head, shoulders, headset)
    random.seed(99)
    dots = []
    
    # Head & Headset (center x=180, y=180)
    for i in range(1200):
        a = random.uniform(0, 2 * math.pi)
        r = math.sqrt(random.uniform(0, 1))
        
        # Part selection
        part = random.choices(['face', 'hair', 'headset', 'shoulders', 'neck'], weights=[0.3, 0.25, 0.15, 0.25, 0.05])[0]
        
        if part == 'face':
            px = 180 + r * 45 * math.cos(a)
            py = 175 + r * 58 * math.sin(a)
        elif part == 'hair':
            px = 180 + r * 50 * math.cos(a)
            py = 150 + r * 42 * math.sin(a)
        elif part == 'headset':
            # Cyber headset / visor band across eyes
            px = random.uniform(140, 220)
            py = random.uniform(160, 172)
        elif part == 'neck':
            px = 180 + random.uniform(-20, 20)
            py = random.uniform(230, 255)
        else: # shoulders
            px = 180 + r * 105 * math.cos(a)
            py = 300 + r * 45 * math.sin(a)
            if py < 250:
                continue

        dots.append((round(px, 1), round(py, 1)))

    # Partition dots into 20 clean animation bands
    num_groups = 20
    dots_per_grp = len(dots) // num_groups
    groups_xml = []
    
    for i in range(num_groups):
        grp_dots = dots[i*dots_per_grp : (i+1)*dots_per_grp]
        dur = round(random.uniform(2.5, 4.0), 2)
        delay = round(random.uniform(0, 1.5), 2)
        color = accent_cyan if i % 3 == 0 else (accent_purple if i % 3 == 1 else accent_pink)
        
        path_d = " ".join([f"M{d[0]} {d[1]}h2v2h-2z" for d in grp_dots])
        grp_str = f'''    <g fill="{color}">
      <animate attributeName="opacity" values="0.4;1;0.6;1;0.4" dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/>
      <path d="{path_d}"/>
    </g>'''
        groups_xml.append(grp_str)

    portrait_dots_html = "\n".join(groups_xml)

    svg_code = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="460" viewBox="0 0 1180 460" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace" role="img" aria-label="Nystic Shadow — profile.sh --live">
  <defs>
    <!-- Main Gradient -->
    <linearGradient id="nystic-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent_cyan}"><animate attributeName="stop-color" values="{accent_cyan};{accent_purple};{accent_pink};{accent_cyan}" dur="8s" repeatCount="indefinite"/></stop>
      <stop offset="50%" stop-color="{accent_purple}"><animate attributeName="stop-color" values="{accent_purple};{accent_pink};{accent_cyan};{accent_purple}" dur="8s" repeatCount="indefinite"/></stop>
      <stop offset="100%" stop-color="{accent_pink}"><animate attributeName="stop-color" values="{accent_pink};{accent_cyan};{accent_purple};{accent_pink}" dur="8s" repeatCount="indefinite"/></stop>
    </linearGradient>

    <!-- Grid Pattern -->
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{grid_stroke}" stroke-width="0.5" stroke-opacity="0.4"/>
      <circle cx="40" cy="0" r="1.5" fill="{accent_cyan}" fill-opacity="0.3"/>
    </pattern>
  </defs>

  <!-- Background -->
  <rect width="1180" height="460" rx="16" fill="{bg_card}" stroke="{border_color}" stroke-width="2"/>
  <rect width="1180" height="460" rx="16" fill="url(#grid)"/>

  <!-- Top Terminal Bar -->
  <path d="M 0 16 C 0 7.163 7.163 0 16 0 L 1164 0 C 1172.837 0 1180 7.163 1180 16 L 1180 44 L 0 44 Z" fill="{header_bg}"/>
  <circle cx="28" cy="22" r="6" fill="#EF4444"/>
  <circle cx="48" cy="22" r="6" fill="#F59E0B"/>
  <circle cx="68" cy="22" r="6" fill="#10B981"/>
  <text x="590" y="27" text-anchor="middle" fill="{text_sub}" font-size="13" font-weight="600">nystic-shadow ~ profile.sh --live</text>
  <line x1="0" y1="44" x2="1180" y2="44" stroke="{border_color}" stroke-width="1"/>

  <!-- LEFT COLUMN: Main Hero Title & Avatar Contour -->
  <g transform="translate(45, 60)">
    <!-- Dot Matrix Cyber Contour -->
    <g transform="translate(260, 10)">
{portrait_dots_html}
    </g>

    <!-- Dev Crest Sign -->
    <g transform="translate(0, 20)">
      <rect width="70" height="70" rx="16" fill="{bg_panel}" stroke="url(#nystic-grad)" stroke-width="2"/>
      <text x="35" y="44" text-anchor="middle" fill="url(#nystic-grad)" font-size="26" font-weight="900" font-family="monospace">&lt;/&gt;</text>
    </g>

    <!-- Main Hero Name: NYSTIC SHADOW -->
    <text x="90" y="55" fill="url(#nystic-grad)" font-size="42" font-weight="900" font-family="'Segoe UI', sans-serif" letter-spacing="1">Nystic Shadow</text>
    <text x="90" y="85" fill="{text_sub}" font-size="16" font-weight="600" font-family="'Segoe UI', sans-serif">Safir Akhtar • 17 y/o Developer &amp; Creative Technologist</text>

    <!-- Skill Tags Grid -->
    <g transform="translate(0, 125)">
      <rect x="0" y="0" width="165" height="32" rx="16" fill="{bg_panel}" stroke="{accent_cyan}" stroke-width="1"/>
      <text x="82.5" y="21" text-anchor="middle" fill="{accent_cyan}" font-size="12.5" font-weight="700" font-family="'Segoe UI', sans-serif">Python · Node · Go</text>

      <rect x="180" y="0" width="165" height="32" rx="16" fill="{bg_panel}" stroke="{accent_purple}" stroke-width="1"/>
      <text x="262.5" y="21" text-anchor="middle" fill="{accent_purple}" font-size="12.5" font-weight="700" font-family="'Segoe UI', sans-serif">Web Dev &amp; Design</text>

      <rect x="360" y="0" width="185" height="32" rx="16" fill="{bg_panel}" stroke="{accent_pink}" stroke-width="1"/>
      <text x="452.5" y="21" text-anchor="middle" fill="{accent_pink}" font-size="12.5" font-weight="700" font-family="'Segoe UI', sans-serif">AI Workflows &amp; Prompts</text>

      <rect x="0" y="44" width="170" height="32" rx="16" fill="{bg_panel}" stroke="{accent_green}" stroke-width="1"/>
      <text x="85" y="65" text-anchor="middle" fill="{accent_green}" font-size="12.5" font-weight="700" font-family="'Segoe UI', sans-serif">UI/UX (Figma / XD)</text>

      <rect x="185" y="44" width="180" height="32" rx="16" fill="{bg_panel}" stroke="{accent_purple}" stroke-width="1"/>
      <text x="275" y="65" text-anchor="middle" fill="{accent_purple}" font-size="12.5" font-weight="700" font-family="'Segoe UI', sans-serif">Graphics (Ps / Ai / CDR)</text>

      <rect x="380" y="44" width="165" height="32" rx="16" fill="{bg_panel}" stroke="{accent_cyan}" stroke-width="1"/>
      <text x="462.5" y="65" text-anchor="middle" fill="{accent_cyan}" font-size="12.5" font-weight="700" font-family="'Segoe UI', sans-serif">Video Editing (Pr / AE)</text>
    </g>

    <!-- Live Status Pill -->
    <g transform="translate(0, 280)">
      <rect width="545" height="75" rx="14" fill="{bg_panel}" stroke="{border_color}" stroke-width="1.5"/>
      <circle cx="28" cy="37.5" r="6" fill="{accent_green}">
        <animate attributeName="opacity" values="1;0.2;1" dur="2s" repeatCount="indefinite"/>
      </circle>
      <circle cx="28" cy="37.5" r="11" fill="none" stroke="{accent_green}" stroke-width="1.5" stroke-opacity="0.5">
        <animate attributeName="r" values="6;14;6" dur="2s" repeatCount="indefinite"/>
        <animate attributeName="stroke-opacity" values="0.8;0;0.8" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text x="50" y="33" fill="{text_main}" font-size="14" font-weight="700" font-family="'Segoe UI', sans-serif">STATUS: <tspan fill="{accent_green}">BUILDING &amp; AUTOMATING</tspan></text>
      <text x="50" y="53" fill="{text_sub}" font-size="12" font-family="'Segoe UI', sans-serif">Full-Stack Systems • Creative Design • AI Workflows</text>
    </g>
  </g>

  <!-- RIGHT COLUMN: Terminal Spec Panel (Guide Format) -->
  <g transform="translate(635, 60)">
    <rect width="500" height="375" rx="14" fill="{header_bg}" stroke="{border_color}" stroke-width="1.5"/>
    
    <path d="M 0 14 C 0 6.268 6.268 0 14 0 L 486 0 C 493.732 0 500 6.268 500 14 L 500 34 L 0 34 Z" fill="{header_bg}"/>
    <text x="250" y="22" text-anchor="middle" fill="{text_sub}" font-size="12.5" font-weight="600">nystic-shadow.json</text>
    <line x1="0" y1="34" x2="500" y2="34" stroke="{border_color}" stroke-width="1"/>

    <!-- Spec Rows -->
    <g transform="translate(20, 26)" font-size="13">
      <text y="32" fill="{accent_purple}" font-weight="700">Brand</text>
      <text x="110" y="32" fill="{leader_color}">......................................</text>
      <text x="460" y="32" text-anchor="end" fill="{text_main}">Nystic Shadow</text>

      <text y="64" fill="{accent_purple}" font-weight="700">Creator</text>
      <text x="110" y="64" fill="{leader_color}">......................................</text>
      <text x="460" y="64" text-anchor="end" fill="{accent_cyan}">Safir Akhtar (Age 17)</text>

      <text y="96" fill="{accent_purple}" font-weight="700">Handle</text>
      <text x="110" y="96" fill="{leader_color}">......................................</text>
      <text x="460" y="96" text-anchor="end" fill="{accent_pink}">@Nystic-Shadow</text>

      <text y="128" fill="{accent_purple}" font-weight="700">Dev.Sign</text>
      <text x="110" y="128" fill="{leader_color}">......................................</text>
      <text x="460" y="128" text-anchor="end" fill="{accent_green}">&lt;/&gt; Full-Stack &amp; Creative</text>

      <text y="160" fill="{accent_purple}" font-weight="700">Core.Lang</text>
      <text x="110" y="160" fill="{leader_color}">......................................</text>
      <text x="460" y="160" text-anchor="end" fill="{accent_cyan}">Python · Node.js · Go</text>

      <text y="192" fill="{accent_purple}" font-weight="700">Web.Dev</text>
      <text x="110" y="192" fill="{leader_color}">......................................</text>
      <text x="460" y="192" text-anchor="end" fill="#60A5FA">HTML5 · CSS3 · JavaScript</text>

      <text y="224" fill="{accent_purple}" font-weight="700">UI/UX.Tools</text>
      <text x="110" y="224" fill="{leader_color}">......................................</text>
      <text x="460" y="224" text-anchor="end" fill="#F0ABFC">Figma · Adobe XD · Canva</text>

      <text y="256" fill="{accent_purple}" font-weight="700">Graphic.Tools</text>
      <text x="110" y="256" fill="{leader_color}">......................................</text>
      <text x="460" y="256" text-anchor="end" fill="{text_sub}">Photoshop · Illustrator · CorelDRAW</text>

      <text y="288" fill="{accent_purple}" font-weight="700">Video.Tools</text>
      <text x="110" y="288" fill="{leader_color}">......................................</text>
      <text x="460" y="288" text-anchor="end" fill="{accent_pink}">Premiere Pro · After Effects</text>

      <text y="320" fill="{accent_purple}" font-weight="700">AI.Skill</text>
      <text x="110" y="320" fill="{leader_color}">......................................</text>
      <text x="460" y="320" text-anchor="end" fill="{accent_green}">Prompt Engineering &amp; Automation</text>
    </g>
  </g>
</svg>'''
    return svg_code

with open(r'C:\Users\SAZUZ\Nystic-Shadow\dark.svg', 'w', encoding='utf-8') as f:
    f.write(build_svg(is_dark=True))

with open(r'C:\Users\SAZUZ\Nystic-Shadow\light.svg', 'w', encoding='utf-8') as f:
    f.write(build_svg(is_dark=False))

print("Clean crisp Nystic Shadow SVGs built successfully!")
