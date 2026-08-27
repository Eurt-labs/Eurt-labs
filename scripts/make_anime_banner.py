import os

svg_template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200" width="800" height="200">
    <defs>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&amp;family=Noto+Sans+JP:wght@700&amp;display=swap');
            
            .bg { fill: #0D1117; }
            
            .text-main {
                font-family: 'Orbitron', sans-serif;
                font-size: 48px;
                font-weight: 700;
                fill: #ffffff;
                text-anchor: middle;
            }
            
            .text-sub {
                font-family: 'Noto Sans JP', sans-serif;
                font-size: 24px;
                fill: #3B82F6;
                text-anchor: middle;
                letter-spacing: 4px;
            }
            
            .glitch {
                animation: glitch 3s linear infinite;
            }
            
            .glitch-1 {
                fill: #0ff;
                animation: glitch-anim-1 2s linear infinite;
                opacity: 0.8;
            }
            
            .glitch-2 {
                fill: #f0f;
                animation: glitch-anim-2 3s linear infinite;
                opacity: 0.8;
            }
            
            @keyframes glitch-anim-1 {
                0% { transform: translate(0); }
                20% { transform: translate(-2px, 1px); }
                40% { transform: translate(-2px, -1px); }
                60% { transform: translate(2px, 1px); }
                80% { transform: translate(2px, -1px); }
                100% { transform: translate(0); }
            }
            
            @keyframes glitch-anim-2 {
                0% { transform: translate(0); }
                20% { transform: translate(2px, -1px); }
                40% { transform: translate(2px, 1px); }
                60% { transform: translate(-2px, -1px); }
                80% { transform: translate(-2px, 1px); }
                100% { transform: translate(0); }
            }

            .scanlines {
                fill: url(#scanlines);
                opacity: 0.1;
                pointer-events: none;
            }
            
            .grid {
                stroke: #3B82F6;
                stroke-width: 1;
                opacity: 0.2;
            }
        </style>
        <pattern id="scanlines" width="4" height="4" patternUnits="userSpaceOnUse">
            <line x1="0" y1="0" x2="4" y2="0" stroke="#fff" stroke-width="2"/>
        </pattern>
        <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none"/>
        </pattern>
    </defs>
    
    <!-- Background -->
    <rect class="bg" width="100%" height="100%" rx="10"/>
    <rect class="grid" width="100%" height="100%" fill="url(#grid)" rx="10"/>
    
    <!-- Japanese Text Subtitle -->
    <text x="400" y="60" class="text-sub">オタク コーダー // ANIME FAN</text>
    
    <!-- Glitch Text -->
    <text x="400" y="130" class="text-main glitch-1">FULL STACK DEVELOPER</text>
    <text x="400" y="130" class="text-main glitch-2">FULL STACK DEVELOPER</text>
    <text x="400" y="130" class="text-main glitch">FULL STACK DEVELOPER</text>
    
    <!-- Decorative Lines -->
    <line x1="100" y1="160" x2="700" y2="160" stroke="#3B82F6" stroke-width="2" stroke-dasharray="20, 10, 5, 5"/>
    <circle cx="100" cy="160" r="4" fill="#3B82F6"/>
    <circle cx="700" cy="160" r="4" fill="#3B82F6"/>
    
    <!-- Scanlines Overlay -->
    <rect class="scanlines" width="100%" height="100%" rx="10"/>
</svg>
"""

def generate_anime_banner():
    with open("anime-banner.svg", "w", encoding="utf-8") as f:
        f.write(svg_template)
    print("Generated anime-banner.svg")

if __name__ == "__main__":
    generate_anime_banner()
