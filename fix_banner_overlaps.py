import base64
from PIL import Image

def get_base64_avatar():
    img = Image.open(r'C:\Users\SAZUZ\Pictures\ChatGPT Image May 10, 2026, 07_50_53 PM.png')
    img_resized = img.resize((400, 400), Image.Resampling.LANCZOS)
    img_resized.save(r'C:\Users\SAZUZ\Nystic-Shadow\avatar_clean.png', format='PNG', optimize=True)

    with open(r'C:\Users\SAZUZ\Nystic-Shadow\avatar_clean.png', 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def build_fixed_svg(is_dark=True):
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

    svg_code = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1180" height="460" viewBox="0 0 1180 460" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace" role="img" aria-label="Nystic Shadow — profile.sh --live">
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

    <!-- Avatar Circular Clip Path -->
    <clipPath id="avatar-clip">
      <circle cx="155" cy="225" r="120"/>
    </clipPath>
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

  <!-- LEFT COLUMN: Character Avatar in Cyber Frame -->
  <g transform="translate(10, 10)">
    <!-- Outer Animated Cyber Rings -->
    <circle cx="155" cy="225" r="132" fill="none" stroke="url(#nystic-grad)" stroke-width="3" stroke-dasharray="12 8">
      <animateTransform attributeName="transform" type="rotate" from="0 155 225" to="360 155 225" dur="20s" repeatCount="indefinite"/>
    </circle>

    <circle cx="155" cy="225" r="125" fill="none" stroke="{accent_cyan}" stroke-width="1.5" stroke-opacity="0.6">
      <animate attributeName="stroke-opacity" values="0.8;0.2;0.8" dur="3s" repeatCount="indefinite"/>
    </circle>

    <!-- Avatar Background Circle -->
    <circle cx="155" cy="225" r="120" fill="{bg_panel}" stroke="{border_color}" stroke-width="2"/>

    <!-- Crystal Clear Character Image Embedded -->
    <image href="data:image/png;base64,{b64_avatar}" x="35" y="105" width="240" height="240" clip-path="url(#avatar-clip)"/>

    <!-- Hero Identity Block -->
    <g transform="translate(305, 52)">
      <!-- Dev Crest Sign -->
      <g transform="translate(0, 0)">
        <rect width="60" height="60" rx="14" fill="{bg_panel}" stroke="url(#nystic-grad)" stroke-width="2"/>
        <text x="30" y="38" text-anchor="middle" fill="url(#nystic-grad)" font-size="22" font-weight="900" font-family="monospace">&lt;/&gt;</text>
      </g>

      <!-- Main Hero Name: NYSTIC SHADOW -->
      <text x="75" y="38" fill="url(#nystic-grad)" font-size="36" font-weight="900" font-family="'Segoe UI', sans-serif" letter-spacing="1">Nystic Shadow</text>
      <text x="75" y="62" fill="{text_sub}" font-size="14.5" font-weight="600" font-family="'Segoe UI', sans-serif">Safir Akhtar • 17 y/o Developer &amp; Creative Technologist</text>

      <!-- Skill Tags Grid -->
      <g transform="translate(0, 90)">
        <rect x="0" y="0" width="160" height="30" rx="15" fill="{bg_panel}" stroke="{accent_cyan}" stroke-width="1"/>
        <text x="80" y="20" text-anchor="middle" fill="{accent_cyan}" font-size="12" font-weight="700" font-family="'Segoe UI', sans-serif">Python · Node · Go</text>

        <rect x="170" y="0" width="165" height="30" rx="15" fill="{bg_panel}" stroke="{accent_purple}" stroke-width="1"/>
        <text x="252.5" y="20" text-anchor="middle" fill="{accent_purple}" font-size="12" font-weight="700" font-family="'Segoe UI', sans-serif">Web Dev &amp; Design</text>

        <rect x="0" y="40" width="165" height="30" rx="15" fill="{bg_panel}" stroke="{accent_green}" stroke-width="1"/>
        <text x="82.5" y="60" text-anchor="middle" fill="{accent_green}" font-size="12" font-weight="700" font-family="'Segoe UI', sans-serif">UI/UX (Figma / XD)</text>

        <rect x="175" y="40" width="160" height="30" rx="15" fill="{bg_panel}" stroke="{accent_pink}" stroke-width="1"/>
        <text x="255" y="60" text-anchor="middle" fill="{accent_pink}" font-size="12" font-weight="700" font-family="'Segoe UI', sans-serif">Graphics &amp; Video</text>
      </g>

      <!-- Live Status Pill -->
      <g transform="translate(0, 195)">
        <rect width="335" height="68" rx="14" fill="{bg_panel}" stroke="{border_color}" stroke-width="1.5"/>
        <circle cx="24" cy="34" r="5" fill="{accent_green}">
          <animate attributeName="opacity" values="1;0.2;1" dur="2s" repeatCount="indefinite"/>
        </circle>
        <circle cx="24" cy="34" r="10" fill="none" stroke="{accent_green}" stroke-width="1.5" stroke-opacity="0.5">
          <animate attributeName="r" values="5;13;5" dur="2s" repeatCount="indefinite"/>
          <animate attributeName="stroke-opacity" values="0.8;0;0.8" dur="2s" repeatCount="indefinite"/>
        </circle>
        <text x="44" y="30" fill="{text_main}" font-size="13" font-weight="700" font-family="'Segoe UI', sans-serif">STATUS: <tspan fill="{accent_green}">SHIPPING &amp; AUTOMATING</tspan></text>
        <text x="44" y="49" fill="{text_sub}" font-size="11.5" font-family="'Segoe UI', sans-serif">Full-Stack Systems • Creative Design • AI Workflows</text>
      </g>
    </g>
  </g>

  <!-- RIGHT COLUMN: Terminal Spec Panel (Fixed Zero Overlap Spacing) -->
  <g transform="translate(660, 56)">
    <rect width="480" height="380" rx="14" fill="{header_bg}" stroke="{border_color}" stroke-width="1.5"/>
    
    <path d="M 0 14 C 0 6.268 6.268 0 14 0 L 466 0 C 473.732 0 480 6.268 480 14 L 480 34 L 0 34 Z" fill="{header_bg}"/>
    <text x="240" y="22" text-anchor="middle" fill="{text_sub}" font-size="12.5" font-weight="600">nystic-shadow.json</text>
    <line x1="0" y1="34" x2="480" y2="34" stroke="{border_color}" stroke-width="1"/>

    <!-- Spec Rows with Precise Non-Overlapping Leaders & Padding -->
    <g transform="translate(20, 24)" font-size="12">
      <!-- Row 1 -->
      <text y="32" fill="{accent_purple}" font-weight="700">Brand</text>
      <text x="75" y="32" fill="{leader_color}">..................................</text>
      <text x="440" y="32" text-anchor="end" fill="{text_main}">Nystic Shadow</text>

      <!-- Row 2 -->
      <text y="64" fill="{accent_purple}" font-weight="700">Creator</text>
      <text x="85" y="64" fill="{leader_color}">............................</text>
      <text x="440" y="64" text-anchor="end" fill="{accent_cyan}">Safir Akhtar (Age 17)</text>

      <!-- Row 3 -->
      <text y="96" fill="{accent_purple}" font-weight="700">Handle</text>
      <text x="80" y="96" fill="{leader_color}">................................</text>
      <text x="440" y="96" text-anchor="end" fill="{accent_pink}">@Nystic-Shadow</text>

      <!-- Row 4 -->
      <text y="128" fill="{accent_purple}" font-weight="700">Dev.Sign</text>
      <text x="95" y="128" fill="{leader_color}">............................</text>
      <text x="440" y="128" text-anchor="end" fill="{accent_green}">&lt;/&gt; Full-Stack &amp; Creative</text>

      <!-- Row 5 -->
      <text y="160" fill="{accent_purple}" font-weight="700">Core.Lang</text>
      <text x="100" y="160" fill="{leader_color}">..........................</text>
      <text x="440" y="160" text-anchor="end" fill="{accent_cyan}">Python · Node.js · Go</text>

      <!-- Row 6 -->
      <text y="192" fill="{accent_purple}" font-weight="700">Web.Dev</text>
      <text x="85" y="192" fill="{leader_color}">...........................</text>
      <text x="440" y="192" text-anchor="end" fill="#60A5FA">HTML5 · CSS3 · JavaScript</text>

      <!-- Row 7 -->
      <text y="224" fill="{accent_purple}" font-weight="700">UI/UX.Tools</text>
      <text x="115" y="224" fill="{leader_color}">.........................</text>
      <text x="440" y="224" text-anchor="end" fill="#F0ABFC">Figma · Adobe XD · Canva</text>

      <!-- Row 8 -->
      <text y="256" fill="{accent_purple}" font-weight="700">Graphics</text>
      <text x="95" y="256" fill="{leader_color}">................</text>
      <text x="440" y="256" text-anchor="end" fill="{text_sub}">Photoshop · Illustrator · CDR</text>

      <!-- Row 9 -->
      <text y="288" fill="{accent_purple}" font-weight="700">Video.Tools</text>
      <text x="115" y="288" fill="{leader_color}">......................</text>
      <text x="440" y="288" text-anchor="end" fill="{accent_pink}">Premiere Pro · After Effects</text>

      <!-- Row 10 -->
      <text y="320" fill="{accent_purple}" font-weight="700">AI.Skill</text>
      <text x="88" y="320" fill="{leader_color}">......................</text>
      <text x="440" y="320" text-anchor="end" fill="{accent_green}">Prompt Engineering &amp; Automation</text>
    </g>
  </g>
</svg>'''
    return svg_code

with open(r'C:\Users\SAZUZ\Nystic-Shadow\dark.svg', 'w', encoding='utf-8') as f:
    f.write(build_fixed_svg(is_dark=True))

with open(r'C:\Users\SAZUZ\Nystic-Shadow\light.svg', 'w', encoding='utf-8') as f:
    f.write(build_fixed_svg(is_dark=False))

print("Fixed zero-overlap SVGs built successfully!")
