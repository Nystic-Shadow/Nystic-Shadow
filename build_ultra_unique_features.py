import base64
from PIL import Image

def get_base64_avatar():
    img = Image.open(r'C:\Users\SAZUZ\Pictures\ChatGPT Image May 10, 2026, 07_50_53 PM.png')
    img_resized = img.resize((360, 360), Image.Resampling.LANCZOS)
    img_resized.save(r'C:\Users\SAZUZ\Nystic-Shadow\avatar_clean.png', format='PNG', optimize=True)

    with open(r'C:\Users\SAZUZ\Nystic-Shadow\avatar_clean.png', 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def build_unique_banner_svg(is_dark=True):
    b64_avatar = get_base64_avatar()
    
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
        eq_fill = "#22D3EE"
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
        eq_fill = "#0891B2"

    # Animated Equalizer Bars for cyber HUD feel
    eq_bars = []
    for i in range(16):
        x = 255 + (i * 6)
        dur = round(1.2 + (i % 5) * 0.3, 2)
        h1 = 8 + (i * 3) % 20
        h2 = 25 - (i * 2) % 18
        eq_bars.append(f'''<rect x="{x}" y="325" width="3.5" height="{h1}" rx="1.5" fill="{eq_fill}" opacity="0.8">
          <animate attributeName="height" values="{h1};{h2};{h1}" dur="{dur}s" repeatCount="indefinite"/>
          <animate attributeName="y" values="{325+(25-h1)};{325+(25-h2)};{325+(25-h1)}" dur="{dur}s" repeatCount="indefinite"/>
        </rect>''')
    
    eq_xml = "\n".join(eq_bars)

    svg_code = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1180" height="420" viewBox="0 0 1180 420" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace" role="img" aria-label="Nystic Shadow — profile.sh --live">
  <defs>
    <!-- Main Animated Gradient -->
    <linearGradient id="nystic-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent_cyan}"><animate attributeName="stop-color" values="{accent_cyan};{accent_purple};{accent_pink};{accent_cyan}" dur="8s" repeatCount="indefinite"/></stop>
      <stop offset="50%" stop-color="{accent_purple}"><animate attributeName="stop-color" values="{accent_purple};{accent_pink};{accent_cyan};{accent_purple}" dur="8s" repeatCount="indefinite"/></stop>
      <stop offset="100%" stop-color="{accent_pink}"><animate attributeName="stop-color" values="{accent_pink};{accent_cyan};{accent_purple};{accent_pink}" dur="8s" repeatCount="indefinite"/></stop>
    </linearGradient>

    <!-- Clean Grid Pattern -->
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{grid_stroke}" stroke-width="0.5" stroke-opacity="0.4"/>
      <circle cx="40" cy="0" r="1.5" fill="{accent_cyan}" fill-opacity="0.3"/>
    </pattern>

    <!-- Avatar Circular Clip Path -->
    <clipPath id="avatar-clip">
      <circle cx="120" cy="210" r="95"/>
    </clipPath>
  </defs>

  <!-- Base Card Background -->
  <rect width="1180" height="420" rx="16" fill="{bg_card}" stroke="{border_color}" stroke-width="2"/>
  <rect width="1180" height="420" rx="16" fill="url(#grid)"/>

  <!-- Top Terminal Bar -->
  <path d="M 0 16 C 0 7.163 7.163 0 16 0 L 1164 0 C 1172.837 0 1180 7.163 1180 16 L 1180 44 L 0 44 Z" fill="{header_bg}"/>
  <circle cx="28" cy="22" r="6" fill="#EF4444"/>
  <circle cx="48" cy="22" r="6" fill="#F59E0B"/>
  <circle cx="68" cy="22" r="6" fill="#10B981"/>
  <text x="590" y="27" text-anchor="middle" fill="{text_sub}" font-size="13" font-weight="600">nystic-shadow ~ profile.sh --live</text>
  <line x1="0" y1="44" x2="1180" y2="44" stroke="{border_color}" stroke-width="1"/>

  <!-- LEFT SECTION: Character Avatar Frame -->
  <g transform="translate(10, 10)">
    <!-- Animated Rotating Cyber Ring -->
    <circle cx="120" cy="210" r="105" fill="none" stroke="url(#nystic-grad)" stroke-width="3" stroke-dasharray="12 8">
      <animateTransform attributeName="transform" type="rotate" from="0 120 210" to="360 120 210" dur="20s" repeatCount="indefinite"/>
    </circle>

    <!-- Outer Glow Circle -->
    <circle cx="120" cy="210" r="100" fill="none" stroke="{accent_cyan}" stroke-width="1.5" stroke-opacity="0.6">
      <animate attributeName="stroke-opacity" values="0.8;0.2;0.8" dur="3s" repeatCount="indefinite"/>
    </circle>

    <!-- Avatar Background Circle -->
    <circle cx="120" cy="210" r="95" fill="{bg_panel}" stroke="{border_color}" stroke-width="2"/>

    <!-- High-Definition Embedded Character Portrait -->
    <image href="data:image/png;base64,{b64_avatar}" x="25" y="115" width="190" height="190" clip-path="url(#avatar-clip)"/>
  </g>

  <!-- MIDDLE SECTION: Clean Hero Identity Block (Minimal & Concise) -->
  <g transform="translate(255, 65)">
    <!-- Dev Sign Crest Box -->
    <g transform="translate(0, 0)">
      <rect width="52" height="52" rx="14" fill="{bg_panel}" stroke="url(#nystic-grad)" stroke-width="2"/>
      <text x="26" y="33" text-anchor="middle" fill="url(#nystic-grad)" font-size="19" font-weight="900" font-family="monospace">&lt;/&gt;</text>
    </g>

    <!-- Main Hero Name & Concise Subtitle -->
    <text x="66" y="34" fill="url(#nystic-grad)" font-size="34" font-weight="900" font-family="'Segoe UI', sans-serif" letter-spacing="1">Nystic Shadow</text>
    <text x="66" y="56" fill="{text_sub}" font-size="14.5" font-weight="600" font-family="'Segoe UI', sans-serif">Safir Akhtar • 17 y/o</text>

    <!-- Concise Skill Pills Grid -->
    <g transform="translate(0, 80)">
      <rect x="0" y="0" width="170" height="32" rx="16" fill="{bg_panel}" stroke="{accent_cyan}" stroke-width="1"/>
      <text x="85" y="21" text-anchor="middle" fill="{accent_cyan}" font-size="12" font-weight="700" font-family="'Segoe UI', sans-serif">Python · Node · Go</text>

      <rect x="182" y="0" width="170" height="32" rx="16" fill="{bg_panel}" stroke="{accent_purple}" stroke-width="1"/>
      <text x="267" y="21" text-anchor="middle" fill="{accent_purple}" font-size="12" font-weight="700" font-family="'Segoe UI', sans-serif">UI/UX &amp; Web Design</text>

      <rect x="0" y="42" width="170" height="32" rx="16" fill="{bg_panel}" stroke="{accent_green}" stroke-width="1"/>
      <text x="85" y="63" text-anchor="middle" fill="{accent_green}" font-size="12" font-weight="700" font-family="'Segoe UI', sans-serif">Graphics &amp; Video</text>

      <rect x="182" y="42" width="170" height="32" rx="16" fill="{bg_panel}" stroke="{accent_pink}" stroke-width="1"/>
      <text x="267" y="63" text-anchor="middle" fill="{accent_pink}" font-size="12" font-weight="700" font-family="'Segoe UI', sans-serif">AI Prompts &amp; Workflows</text>
    </g>

    <!-- Clean Live Status Pill with Audio Equalizer -->
    <g transform="translate(0, 205)">
      <rect width="352" height="64" rx="14" fill="{bg_panel}" stroke="{border_color}" stroke-width="1.5"/>
      <circle cx="22" cy="32" r="5" fill="{accent_green}">
        <animate attributeName="opacity" values="1;0.2;1" dur="2s" repeatCount="indefinite"/>
      </circle>
      <circle cx="22" cy="32" r="10" fill="none" stroke="{accent_green}" stroke-width="1.5" stroke-opacity="0.5">
        <animate attributeName="r" values="5;13;5" dur="2s" repeatCount="indefinite"/>
        <animate attributeName="stroke-opacity" values="0.8;0;0.8" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text x="42" y="28" fill="{text_main}" font-size="12.5" font-weight="700" font-family="'Segoe UI', sans-serif">STATUS: <tspan fill="{accent_green}">SHIPPING &amp; AUTOMATING</tspan></text>
      <text x="42" y="46" fill="{text_sub}" font-size="11" font-family="'Segoe UI', sans-serif">Full-Stack Engineering • Creative Design • AI Skills</text>
    </g>
  </g>

  <!-- RIGHT SECTION: Clean Minimal Terminal Spec Panel -->
  <g transform="translate(640, 65)">
    <rect width="495" height="325" rx="14" fill="{header_bg}" stroke="{border_color}" stroke-width="1.5"/>
    
    <path d="M 0 14 C 0 6.268 6.268 0 14 0 L 481 0 C 488.732 0 495 6.268 495 14 L 495 34 L 0 34 Z" fill="{header_bg}"/>
    <text x="247.5" y="22" text-anchor="middle" fill="{text_sub}" font-size="12.5" font-weight="600">nystic-shadow.json</text>
    <line x1="0" y1="34" x2="495" y2="34" stroke="{border_color}" stroke-width="1"/>

    <!-- Concise Spec Rows -->
    <g transform="translate(22, 24)" font-size="12.5">
      <text y="34" fill="{accent_purple}" font-weight="700">Brand</text>
      <text x="75" y="34" fill="{leader_color}">......................................</text>
      <text x="450" y="34" text-anchor="end" fill="{text_main}">Nystic Shadow</text>

      <text y="72" fill="{accent_purple}" font-weight="700">Creator</text>
      <text x="85" y="72" fill="{leader_color}">................................</text>
      <text x="450" y="72" text-anchor="end" fill="{accent_cyan}">Safir Akhtar (Age 17)</text>

      <text y="110" fill="{accent_purple}" font-weight="700">Handle</text>
      <text x="80" y="110" fill="{leader_color}">..................................</text>
      <text x="450" y="110" text-anchor="end" fill="{accent_pink}">@Nystic-Shadow</text>

      <text y="148" fill="{accent_purple}" font-weight="700">Dev.Sign</text>
      <text x="95" y="148" fill="{leader_color}">............................</text>
      <text x="450" y="148" text-anchor="end" fill="{accent_green}">&lt;/&gt; Developer &amp; Designer</text>

      <text y="186" fill="{accent_purple}" font-weight="700">Core.Lang</text>
      <text x="100" y="186" fill="{leader_color}">..........................</text>
      <text x="450" y="186" text-anchor="end" fill="{accent_cyan}">Python · Node.js · Go · JS</text>

      <text y="224" fill="{accent_purple}" font-weight="700">Creative</text>
      <text x="95" y="224" fill="{leader_color}">..........................</text>
      <text x="450" y="224" text-anchor="end" fill="#F0ABFC">UI/UX · Adobe Suite · AI Skill</text>

      <text y="262" fill="{accent_purple}" font-weight="700">Tools</text>
      <text x="75" y="262" fill="{leader_color}">......................................</text>
      <text x="450" y="262" text-anchor="end" fill="{text_sub}">VS Code · Git · Figma</text>
    </g>
  </g>
</svg>'''
    return svg_code

# Also generate a custom projects.svg showcase card (matching arifhaxn's projects showcase card!)
def build_projects_svg():
    svg_code = '''<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="220" viewBox="0 0 1180 220" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace" role="img" aria-label="Nystic Shadow — Specialization Pillars">
  <defs>
    <linearGradient id="p-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#22D3EE"/>
      <stop offset="50%" stop-color="#A78BFA"/>
      <stop offset="100%" stop-color="#F472B6"/>
    </linearGradient>
    <linearGradient id="p-card" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0A101F"/>
      <stop offset="1" stop-color="#0C1426"/>
    </linearGradient>
  </defs>

  <rect width="1180" height="220" rx="16" fill="url(#p-card)" stroke="#1E293B" stroke-width="2"/>

  <!-- Header Title -->
  <text x="40" y="42" fill="url(#p-grad)" font-size="20" font-weight="800" font-family="'Segoe UI', sans-serif">🚀 SPECIALIZATION PILLARS &amp; EXPERTISE</text>
  <line x1="40" y1="56" x2="1140" y2="56" stroke="#1E293B" stroke-width="1"/>

  <!-- 4 Pillars Grid -->
  <!-- Pillar 1: Full-Stack -->
  <g transform="translate(40, 75)">
    <rect width="255" height="115" rx="12" fill="#040711" stroke="#22D3EE" stroke-width="1"/>
    <text x="20" y="32" fill="#22D3EE" font-size="14" font-weight="700" font-family="'Segoe UI', sans-serif">💻 Full-Stack Dev</text>
    <text x="20" y="56" fill="#F8FAFC" font-size="12">Python · Node.js · Go</text>
    <text x="20" y="76" fill="#94A3B8" font-size="11">Scalable Web &amp; REST APIs</text>
    <text x="20" y="96" fill="#10B981" font-size="11" font-weight="600">🟢 Active Engineering</text>
  </g>

  <!-- Pillar 2: AI Workflows -->
  <g transform="translate(325, 75)">
    <rect width="255" height="115" rx="12" fill="#040711" stroke="#A78BFA" stroke-width="1"/>
    <text x="20" y="32" fill="#A78BFA" font-size="14" font-weight="700" font-family="'Segoe UI', sans-serif">🤖 AI &amp; Automation</text>
    <text x="20" y="56" fill="#F8FAFC" font-size="12">Prompt Engineering</text>
    <text x="20" y="76" fill="#94A3B8" font-size="11">LLM &amp; Agent Workflows</text>
    <text x="20" y="96" fill="#A78BFA" font-size="11" font-weight="600">⚡ LLM Architect</text>
  </g>

  <!-- Pillar 3: UI/UX & 3D -->
  <g transform="translate(610, 75)">
    <rect width="255" height="115" rx="12" fill="#040711" stroke="#F472B6" stroke-width="1"/>
    <text x="20" y="32" fill="#F472B6" font-size="14" font-weight="700" font-family="'Segoe UI', sans-serif">🎨 UI/UX &amp; Web Design</text>
    <text x="20" y="56" fill="#F8FAFC" font-size="12">Figma · XD · Canva · CDR</text>
    <text x="20" y="76" fill="#94A3B8" font-size="11">Design Systems &amp; Prototyping</text>
    <text x="20" y="96" fill="#F472B6" font-size="11" font-weight="600">✨ Visual Artist</text>
  </g>

  <!-- Pillar 4: Video Editing -->
  <g transform="translate(895, 75)">
    <rect width="245" height="115" rx="12" fill="#040711" stroke="#10B981" stroke-width="1"/>
    <text x="20" y="32" fill="#10B981" font-size="14" font-weight="700" font-family="'Segoe UI', sans-serif">🎬 Video &amp; Motion</text>
    <text x="20" y="56" fill="#F8FAFC" font-size="12">Premiere Pro · After Effects</text>
    <text x="20" y="76" fill="#94A3B8" font-size="11">Cinematic VFX &amp; Edits</text>
    <text x="20" y="96" fill="#10B981" font-size="11" font-weight="600">🎥 Post-Production</text>
  </g>
</svg>'''
    with open(r'C:\Users\SAZUZ\Nystic-Shadow\projects.svg', 'w', encoding='utf-8') as f:
        f.write(svg_code)
    print("Generated projects.svg successfully!")

with open(r'C:\Users\SAZUZ\Nystic-Shadow\dark.svg', 'w', encoding='utf-8') as f:
    f.write(build_unique_banner_svg(is_dark=True))

with open(r'C:\Users\SAZUZ\Nystic-Shadow\light.svg', 'w', encoding='utf-8') as f:
    f.write(build_unique_banner_svg(is_dark=False))

build_projects_svg()
print("Ultra-unique SVGs generated successfully!")
