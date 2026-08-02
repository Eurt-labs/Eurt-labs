import os

def generate_info_card():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="490" height="417" viewBox="0 0 490 417" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
    <defs>
        <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0" stop-color="#111722"/>
            <stop offset="1" stop-color="#0d1117"/>
        </linearGradient>
    </defs>
    <rect width="490" height="417" rx="12" fill="url(#bg)"/>
    <rect x="0.5" y="0.5" width="489" height="416" rx="12" fill="none" stroke="#30363d" stroke-width="1"/>
    
    <line x1="0" y1="28" x2="490" y2="28" stroke="#30363d"/>
    <circle cx="18" cy="14" r="4.5" fill="#ff5f56"/>
    <circle cx="33" cy="14" r="4.5" fill="#ffbd2e"/>
    <circle cx="48" cy="14" r="4.5" fill="#27c93f"/>
    <text x="245" y="18" fill="#7d8590" font-size="11.5" text-anchor="middle">dhruv@github: ~$ neofetch</text>

    <!-- Content -->
    <g font-size="14" fill="#c9d1d9">
        <!-- Fade in animations -->
        <g opacity="0"><animate attributeName="opacity" to="1" dur="0.2s" begin="0.3s" fill="freeze"/>
            <text x="30" y="70" fill="#27c93f" font-weight="bold">dhruv@github</text>
            <text x="30" y="85">------------</text>
        </g>
        
        <g opacity="0"><animate attributeName="opacity" to="1" dur="0.2s" begin="0.5s" fill="freeze"/>
            <text x="30" y="115"><tspan fill="#ffbd2e" font-weight="bold">OS</tspan>: Linux</text>
        </g>
        
        <g opacity="0"><animate attributeName="opacity" to="1" dur="0.2s" begin="0.7s" fill="freeze"/>
            <text x="30" y="145"><tspan fill="#ffbd2e" font-weight="bold">Host</tspan>: Dhruv Sharma</text>
        </g>
        
        <g opacity="0"><animate attributeName="opacity" to="1" dur="0.2s" begin="0.9s" fill="freeze"/>
            <text x="30" y="175"><tspan fill="#ffbd2e" font-weight="bold">Role</tspan>: AI, Machine learning and Networks </text>
        </g>
        
        <g opacity="0"><animate attributeName="opacity" to="1" dur="0.2s" begin="1.1s" fill="freeze"/>
            <text x="30" y="205"><tspan fill="#ffbd2e" font-weight="bold">Location</tspan>: New Delhi, India 🇮🇳</text>
        </g>
        
        <g opacity="0"><animate attributeName="opacity" to="1" dur="0.2s" begin="1.3s" fill="freeze"/>
            <text x="30" y="235"><tspan fill="#ffbd2e" font-weight="bold">Learning</tspan>: AI/ML, Networking, EdgeAI and IoT </text>
        </g>

        <g opacity="0"><animate attributeName="opacity" to="1" dur="0.2s" begin="1.5s" fill="freeze"/>
            <text x="30" y="265"><tspan fill="#ffbd2e" font-weight="bold">Tech Stack</tspan>: C/C++, Python, React, PyTorch and TensorFlow.</text>
        </g>

        <g opacity="0"><animate attributeName="opacity" to="1" dur="0.2s" begin="1.7s" fill="freeze"/>
            <text x="30" y="295"><tspan fill="#ffbd2e" font-weight="bold">Portfolio</tspan>: https://dhruvv.app</text>
        </g>

        <g opacity="0"><animate attributeName="opacity" to="1" dur="0.2s" begin="1.9s" fill="freeze"/>
            <text x="30" y="325"><tspan fill="#ffbd2e" font-weight="bold">College</tspan>: Gautam Buddha University </text>
        </g>

        <!-- Color blocks -->
        <g opacity="0"><animate attributeName="opacity" to="1" dur="0.2s" begin="2.1s" fill="freeze"/>
            <rect x="30" y="355" width="20" height="20" fill="#0d1117"/>
            <rect x="55" y="355" width="20" height="20" fill="#ff5f56"/>
            <rect x="80" y="355" width="20" height="20" fill="#27c93f"/>
            <rect x="105" y="355" width="20" height="20" fill="#ffbd2e"/>
            <rect x="130" y="355" width="20" height="20" fill="#181717"/>
            <rect x="155" y="355" width="20" height="20" fill="#c9d1d9"/>
        </g>
    </g>
</svg>"""
    
    with open("info-card.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("info-card.svg generated")

if __name__ == "__main__":
    generate_info_card()
