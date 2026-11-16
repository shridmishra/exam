# scratch/theory_svgs.py
"""
High-quality, responsive SVG diagrams for Geotechnical Engineering theory solutions.
Styled using CSS variables (--foreground, --muted-foreground, --secondary, --card, etc.)
so they automatically adapt to both light mode and dark mode.
"""

SVG_MODES_OF_SHEAR_FAILURE = '''<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Modes of Shear Failure &amp; Rupture Surfaces</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 230" class="sol-diagram-svg" width="100%" style="max-width:680px;height:auto;display:block;">
    <rect width="680" height="230" fill="var(--card)" rx="8" />
    
    <!-- Panel 1: General Shear -->
    <g transform="translate(15, 10)">
      <rect x="0" y="0" width="205" height="210" fill="var(--secondary)" rx="6" opacity="0.5" />
      <text x="102" y="22" fill="var(--foreground)" font-size="12" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">General Shear Failure</text>
      <text x="102" y="37" fill="var(--muted-foreground)" font-size="10" text-anchor="middle" font-family="system-ui, sans-serif">Dense Sand (Dr &gt; 70%) / Stiff Clay</text>
      
      <!-- Heave profiles -->
      <path d="M 15 90 Q 45 75 75 90" fill="none" stroke="var(--muted-foreground)" stroke-width="1.5" stroke-dasharray="2 2" />
      <path d="M 130 90 Q 160 75 190 90" fill="none" stroke="var(--muted-foreground)" stroke-width="1.5" stroke-dasharray="2 2" />
      <line x1="10" y1="90" x2="195" y2="90" stroke="var(--muted-foreground)" stroke-width="1" />
      
      <!-- Footing -->
      <rect x="75" y="72" width="55" height="18" fill="var(--foreground)" opacity="0.85" rx="2" />
      <text x="102" y="84" fill="var(--primary-foreground)" font-size="9" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Footing (B)</text>
      
      <!-- Elastic wedge -->
      <polygon points="75,90 130,90 102.5,120" fill="var(--muted-foreground)" opacity="0.2" stroke="var(--foreground)" stroke-width="1.2" />
      
      <!-- Continuous failure planes reaching surface -->
      <path d="M 102.5 120 Q 50 125 15 90" fill="none" stroke="var(--foreground)" stroke-width="1.8" />
      <path d="M 102.5 120 Q 155 125 190 90" fill="none" stroke="var(--foreground)" stroke-width="1.8" />
      
      <!-- Features bullets -->
      <text x="15" y="150" fill="var(--foreground)" font-size="10" font-family="system-ui, sans-serif">• Continuous well-defined rupture</text>
      <text x="15" y="168" fill="var(--foreground)" font-size="10" font-family="system-ui, sans-serif">• Significant surface heave/bulging</text>
      <text x="15" y="186" fill="var(--foreground)" font-size="10" font-family="system-ui, sans-serif">• Sudden, catastrophic tilting</text>
      <text x="15" y="202" fill="var(--pastel-peach-foreground, #f97316)" font-size="9.5" font-weight="bold" font-family="system-ui, sans-serif">Distinct peak load (qu)</text>
    </g>

    <!-- Panel 2: Local Shear -->
    <g transform="translate(235, 10)">
      <rect x="0" y="0" width="205" height="210" fill="var(--secondary)" rx="6" opacity="0.5" />
      <text x="102" y="22" fill="var(--foreground)" font-size="12" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Local Shear Failure</text>
      <text x="102" y="37" fill="var(--muted-foreground)" font-size="10" text-anchor="middle" font-family="system-ui, sans-serif">Medium Sand (35% &lt; Dr &lt; 70%)</text>
      
      <!-- Slight heave -->
      <path d="M 25 90 Q 50 82 75 90" fill="none" stroke="var(--muted-foreground)" stroke-width="1.5" stroke-dasharray="2 2" />
      <path d="M 130 90 Q 155 82 180 90" fill="none" stroke="var(--muted-foreground)" stroke-width="1.5" stroke-dasharray="2 2" />
      <line x1="10" y1="90" x2="195" y2="90" stroke="var(--muted-foreground)" stroke-width="1" />
      
      <!-- Footing -->
      <rect x="75" y="72" width="55" height="18" fill="var(--foreground)" opacity="0.85" rx="2" />
      <text x="102" y="84" fill="var(--primary-foreground)" font-size="9" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Footing (B)</text>
      
      <!-- Elastic wedge -->
      <polygon points="75,90 130,90 102.5,115" fill="var(--muted-foreground)" opacity="0.2" stroke="var(--foreground)" stroke-width="1.2" />
      
      <!-- Slip surfaces ending in soil -->
      <path d="M 102.5 115 Q 60 120 35 105" fill="none" stroke="var(--foreground)" stroke-width="1.8" stroke-dasharray="4 2" />
      <path d="M 102.5 115 Q 145 120 170 105" fill="none" stroke="var(--foreground)" stroke-width="1.8" stroke-dasharray="4 2" />
      
      <!-- Features bullets -->
      <text x="15" y="150" fill="var(--foreground)" font-size="10" font-family="system-ui, sans-serif">• Rupture ends inside soil mass</text>
      <text x="15" y="168" fill="var(--foreground)" font-size="10" font-family="system-ui, sans-serif">• Minor / slight ground heave</text>
      <text x="15" y="186" fill="var(--foreground)" font-size="10" font-family="system-ui, sans-serif">• Significant progressive settlement</text>
      <text x="15" y="202" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="9.5" font-weight="bold" font-family="system-ui, sans-serif">No distinct peak on curve</text>
    </g>

    <!-- Panel 3: Punching Shear -->
    <g transform="translate(455, 10)">
      <rect x="0" y="0" width="210" height="210" fill="var(--secondary)" rx="6" opacity="0.5" />
      <text x="105" y="22" fill="var(--foreground)" font-size="12" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Punching Shear Failure</text>
      <text x="105" y="37" fill="var(--muted-foreground)" font-size="10" text-anchor="middle" font-family="system-ui, sans-serif">Loose Sand (Dr &lt; 35%) / Soft Clay</text>
      
      <!-- Flat ground (zero heave) -->
      <line x1="10" y1="75" x2="200" y2="75" stroke="var(--muted-foreground)" stroke-width="1" />
      
      <!-- Footing plunged down -->
      <rect x="77" y="88" width="55" height="18" fill="var(--foreground)" opacity="0.85" rx="2" />
      <text x="105" y="100" fill="var(--primary-foreground)" font-size="9" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Footing (B)</text>
      
      <!-- Vertical shear failure lines -->
      <line x1="77" y1="75" x2="77" y2="135" stroke="var(--foreground)" stroke-width="1.8" stroke-dasharray="3 3" />
      <line x1="132" y1="75" x2="132" y2="135" stroke="var(--foreground)" stroke-width="1.8" stroke-dasharray="3 3" />
      <polygon points="77,106 132,106 104.5,125" fill="var(--muted-foreground)" opacity="0.15" stroke="var(--foreground)" stroke-width="1" />
      
      <!-- Features bullets -->
      <text x="15" y="150" fill="var(--foreground)" font-size="10" font-family="system-ui, sans-serif">• Vertical shearing around edges</text>
      <text x="15" y="168" fill="var(--foreground)" font-size="10" font-family="system-ui, sans-serif">• Zero heave / no surface bulging</text>
      <text x="15" y="186" fill="var(--foreground)" font-size="10" font-family="system-ui, sans-serif">• Continuous plunging settlement</text>
      <text x="15" y="202" fill="var(--pastel-lavender-foreground, #a855f7)" font-size="9.5" font-weight="bold" font-family="system-ui, sans-serif">Linear-elastic then plunge</text>
    </g>
  </svg>
</div>'''

SVG_LOAD_SETTLEMENT_CURVES = '''<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Load-Settlement (q vs s) Curves for Modes of Failure</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 240" class="sol-diagram-svg" width="100%" style="max-width:460px;height:auto;display:block;">
    <rect width="460" height="240" fill="var(--card)" rx="8" />
    <g transform="translate(50, 25)">
      <!-- Axes -->
      <line x1="0" y1="170" x2="370" y2="170" stroke="var(--foreground)" stroke-width="1.5" />
      <line x1="0" y1="170" x2="0" y2="10" stroke="var(--foreground)" stroke-width="1.5" />
      <polygon points="370,170 362,166 362,174" fill="var(--foreground)" />
      <polygon points="0,10 -4,18 4,18" fill="var(--foreground)" />
      
      <text x="365" y="190" fill="var(--foreground)" font-size="11" font-weight="bold" text-anchor="end" font-family="system-ui, sans-serif">Settlement s →</text>
      <text x="-10" y="15" fill="var(--foreground)" font-size="11" font-weight="bold" text-anchor="end" font-family="system-ui, sans-serif">Load / Pressure q ↑</text>
      
      <line x1="0" y1="50" x2="350" y2="50" stroke="var(--muted-foreground)" stroke-width="0.5" stroke-dasharray="3 3" opacity="0.4" />
      <line x1="0" y1="100" x2="350" y2="100" stroke="var(--muted-foreground)" stroke-width="0.5" stroke-dasharray="3 3" opacity="0.4" />
      
      <!-- Curve 1: General Shear (Sharp Peak qu, then drop) -->
      <path d="M 0 170 C 40 70, 70 35, 110 35 C 130 35, 160 70, 240 85" fill="none" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2.5" />
      <circle cx="110" cy="35" r="4" fill="var(--pastel-peach-foreground, #f97316)" />
      <text x="115" y="28" fill="var(--pastel-peach-foreground, #f97316)" font-size="10.5" font-weight="bold" font-family="system-ui, sans-serif">Peak qu (General)</text>
      
      <!-- Curve 2: Local Shear (Transitional, no distinct peak) -->
      <path d="M 0 170 C 60 120, 140 85, 260 70" fill="none" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2.5" stroke-dasharray="6 3" />
      <text x="265" y="68" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="10.5" font-weight="bold" font-family="system-ui, sans-serif">Local Shear</text>
      
      <!-- Curve 3: Punching Shear (Plunging downwards) -->
      <path d="M 0 170 C 80 150, 160 130, 280 105" fill="none" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="2.5" stroke-dasharray="2 2" />
      <text x="285" y="108" fill="var(--pastel-lavender-foreground, #a855f7)" font-size="10.5" font-weight="bold" font-family="system-ui, sans-serif">Punching Shear</text>
      
      <!-- Legend -->
      <g transform="translate(15, 205)">
        <circle cx="0" cy="0" r="4" fill="var(--pastel-peach-foreground, #f97316)" />
        <text x="8" y="3" fill="var(--foreground)" font-size="10" font-family="system-ui, sans-serif">General (Dense)</text>
        <line x1="115" y1="0" x2="130" y2="0" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2.5" stroke-dasharray="4 2" />
        <text x="136" y="3" fill="var(--foreground)" font-size="10" font-family="system-ui, sans-serif">Local (Medium)</text>
        <line x1="230" y1="0" x2="245" y2="0" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="2.5" stroke-dasharray="2 2" />
        <text x="251" y="3" fill="var(--foreground)" font-size="10" font-family="system-ui, sans-serif">Punching (Loose)</text>
      </g>
    </g>
  </svg>
</div>'''

SVG_OPEN_CAISSON = '''<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Cross-Section of Open Caisson (Well Foundation) Components</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 360" class="sol-diagram-svg" width="100%" style="max-width:420px;height:auto;display:block;">
    <rect width="420" height="360" fill="var(--card)" rx="8" />
    <g transform="translate(30, 20)">
      <!-- Well Cap -->
      <rect x="60" y="10" width="200" height="24" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.5" rx="3" />
      <text x="160" y="26" fill="var(--foreground)" font-size="11" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Well Cap (Transfers Superstructure Load)</text>
      
      <!-- Left Steining Wall -->
      <rect x="75" y="34" width="36" height="220" fill="var(--muted)" stroke="var(--foreground)" stroke-width="1.5" />
      <!-- Right Steining Wall -->
      <rect x="209" y="34" width="36" height="220" fill="var(--muted)" stroke="var(--foreground)" stroke-width="1.5" />
      
      <!-- Top Plug -->
      <rect x="111" y="45" width="98" height="22" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.2" />
      <text x="160" y="60" fill="var(--muted-foreground)" font-size="9.5" text-anchor="middle" font-family="system-ui, sans-serif">Top Plug (Concrete Seal)</text>
      
      <!-- Sand Filling -->
      <rect x="111" y="67" width="98" height="145" fill="var(--card)" stroke="none" />
      <path d="M 115 85 L 205 85 M 115 110 L 205 110 M 115 135 L 205 135 M 115 160 L 205 160 M 115 185 L 205 185" stroke="var(--muted-foreground)" stroke-width="0.5" stroke-dasharray="2 4" opacity="0.5" />
      <text x="160" y="145" fill="var(--muted-foreground)" font-size="11" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Sand Filling (Ballast)</text>
      
      <!-- Bottom Plug (Tremie Concrete) -->
      <path d="M 111 212 Q 160 195 209 212 L 209 254 L 111 254 Z" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.2" />
      <text x="160" y="238" fill="var(--foreground)" font-size="10" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Bottom Plug (Tremie Concrete)</text>
      
      <!-- Left Well Curb (Tapered Wedge) -->
      <polygon points="75,254 111,254 75,285" fill="var(--muted)" stroke="var(--foreground)" stroke-width="1.5" />
      <!-- Right Well Curb (Tapered Wedge) -->
      <polygon points="209,254 245,254 245,285" fill="var(--muted)" stroke="var(--foreground)" stroke-width="1.5" />
      
      <!-- Left Cutting Edge -->
      <polygon points="75,285 85,285 75,298" fill="var(--foreground)" />
      <!-- Right Cutting Edge -->
      <polygon points="245,285 235,285 245,298" fill="var(--foreground)" />
      
      <!-- Labels with Leader Lines -->
      <line x1="55" y1="120" x2="75" y2="120" stroke="var(--foreground)" stroke-width="1" />
      <text x="50" y="124" fill="var(--foreground)" font-size="10" font-weight="bold" text-anchor="end" font-family="system-ui, sans-serif">Steining Wall (Self-weight)</text>
      
      <line x1="220" y1="100" x2="280" y2="100" stroke="var(--foreground)" stroke-width="1" />
      <text x="285" y="104" fill="var(--foreground)" font-size="10" font-weight="bold" font-family="system-ui, sans-serif">Central Dredge Hole</text>
      
      <line x1="245" y1="268" x2="280" y2="268" stroke="var(--foreground)" stroke-width="1" />
      <text x="285" y="272" fill="var(--foreground)" font-size="10" font-weight="bold" font-family="system-ui, sans-serif">Well Curb (RCC Wedge)</text>
      
      <line x1="245" y1="292" x2="280" y2="292" stroke="var(--foreground)" stroke-width="1" />
      <text x="285" y="296" fill="var(--foreground)" font-size="10" font-weight="bold" font-family="system-ui, sans-serif">Cutting Edge (Steel Shoe)</text>
      
      <!-- Founding Strata Baseline -->
      <line x1="30" y1="298" x2="290" y2="298" stroke="var(--muted-foreground)" stroke-width="1.5" stroke-dasharray="4 2" />
      <text x="160" y="316" fill="var(--muted-foreground)" font-size="9.5" text-anchor="middle" font-family="system-ui, sans-serif">Founding Stratum (Hard Rock / Dense Gravel)</text>
    </g>
  </svg>
</div>'''

SVG_STRAP_FOOTING = '''<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Elevation &amp; Structural Action of Strap (Cantilever) Footing</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" class="sol-diagram-svg" width="100%" style="max-width:520px;height:auto;display:block;">
    <rect width="520" height="220" fill="var(--card)" rx="8" />
    <g transform="translate(25, 20)">
      <!-- Property Line -->
      <line x1="25" y1="10" x2="25" y2="180" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2" stroke-dasharray="6 3" />
      <text x="20" y="20" fill="var(--pastel-peach-foreground, #f97316)" font-size="10" font-weight="bold" text-anchor="end" font-family="system-ui, sans-serif">Property Line</text>
      <text x="20" y="32" fill="var(--muted-foreground)" font-size="8.5" text-anchor="end" font-family="system-ui, sans-serif">(Zero encroachment)</text>
      
      <!-- Exterior Column (Column 1) -->
      <rect x="25" y="35" width="24" height="45" fill="var(--foreground)" opacity="0.9" />
      <text x="37" y="28" fill="var(--foreground)" font-size="10.5" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Col 1 (P1)</text>
      
      <!-- Exterior Footing (Eccentric) -->
      <rect x="25" y="80" width="85" height="28" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.5" />
      <text x="67" y="98" fill="var(--foreground)" font-size="10" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Eccentric Footing</text>
      
      <!-- Interior Column (Column 2) -->
      <rect x="350" y="35" width="26" height="45" fill="var(--foreground)" opacity="0.9" />
      <text x="363" y="28" fill="var(--foreground)" font-size="10.5" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Col 2 (P2)</text>
      
      <!-- Interior Footing (Concentric) -->
      <rect x="305" y="80" width="115" height="28" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.5" />
      <text x="363" y="98" fill="var(--foreground)" font-size="10" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Concentric Footing</text>
      
      <!-- Rigid Strap Beam -->
      <rect x="35" y="60" width="330" height="22" fill="var(--muted)" stroke="var(--foreground)" stroke-width="1.8" rx="2" />
      <text x="200" y="75" fill="var(--foreground)" font-size="10.5" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Rigid Strap Beam (Cantilever Moment Transfer)</text>
      
      <!-- Air Gap / No soil pressure indicator -->
      <rect x="110" y="82" width="195" height="18" fill="none" stroke="var(--muted-foreground)" stroke-width="1" stroke-dasharray="3 3" />
      <text x="207" y="95" fill="var(--muted-foreground)" font-size="9" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">AIR GAP: No contact with soil underneath</text>
      <text x="207" y="106" fill="var(--muted-foreground)" font-size="8" text-anchor="middle" font-family="system-ui, sans-serif">(Transfers shear &amp; moment only; zero upward bearing)</text>
      
      <!-- Soil Reaction Arrows -->
      <line x1="45" y1="130" x2="45" y2="110" stroke="var(--foreground)" stroke-width="1.5" />
      <polygon points="45,108 42,115 48,115" fill="var(--foreground)" />
      <line x1="67" y1="130" x2="67" y2="110" stroke="var(--foreground)" stroke-width="1.5" />
      <polygon points="67,108 64,115 70,115" fill="var(--foreground)" />
      <line x1="90" y1="130" x2="90" y2="110" stroke="var(--foreground)" stroke-width="1.5" />
      <polygon points="90,108 87,115 93,115" fill="var(--foreground)" />
      <text x="67" y="145" fill="var(--foreground)" font-size="9.5" text-anchor="middle" font-family="system-ui, sans-serif">Soil Reaction R1</text>
      
      <line x1="325" y1="130" x2="325" y2="110" stroke="var(--foreground)" stroke-width="1.5" />
      <polygon points="325,108 322,115 328,115" fill="var(--foreground)" />
      <line x1="363" y1="130" x2="363" y2="110" stroke="var(--foreground)" stroke-width="1.5" />
      <polygon points="363,108 360,115 366,115" fill="var(--foreground)" />
      <line x1="400" y1="130" x2="400" y2="110" stroke="var(--foreground)" stroke-width="1.5" />
      <polygon points="400,108 397,115 403,115" fill="var(--foreground)" />
      <text x="363" y="145" fill="var(--foreground)" font-size="9.5" text-anchor="middle" font-family="system-ui, sans-serif">Soil Reaction R2</text>
      
      <!-- Design Criterion Note -->
      <text x="235" y="175" fill="var(--foreground)" font-size="9.5" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Key Mechanism: Strap beam restrains rotation of eccentric exterior footing</text>
    </g>
  </svg>
</div>'''

SVG_REBHANN_CONSTRUCTION = '''<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Rebhann's Graphical Construction for Active Thrust (Pa)</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 270" class="sol-diagram-svg" width="100%" style="max-width:500px;height:auto;display:block;">
    <rect width="500" height="270" fill="var(--card)" rx="8" />
    <g transform="translate(30, 20)">
      <line x1="20" y1="200" x2="430" y2="200" stroke="var(--muted-foreground)" stroke-width="1" stroke-dasharray="3 3" />
      <line x1="60" y1="70" x2="60" y2="200" stroke="var(--foreground)" stroke-width="2.5" />
      <path d="M 45 70 L 60 70 M 45 95 L 60 95 M 45 120 L 60 120 M 45 145 L 60 145 M 45 170 L 60 170 M 45 195 L 60 195" stroke="var(--muted-foreground)" stroke-width="1.2" />
      <text x="50" y="65" fill="var(--foreground)" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">A (Crest)</text>
      <text x="50" y="215" fill="var(--foreground)" font-size="12" font-weight="bold" font-family="system-ui, sans-serif">B (Heel)</text>
      
      <line x1="60" y1="70" x2="390" y2="70" stroke="var(--foreground)" stroke-width="2" />
      <text x="400" y="75" fill="var(--foreground)" font-size="11" font-weight="bold" font-family="system-ui, sans-serif">D (Ground Line)</text>
      
      <line x1="60" y1="200" x2="390" y2="70" stroke="var(--muted-foreground)" stroke-width="1.5" />
      <text x="245" y="120" fill="var(--muted-foreground)" font-size="10" font-weight="bold" font-family="system-ui, sans-serif">φ-line (angle φ)</text>
      
      <path d="M 60 200 A 177 177 0 0 1 390 70" fill="none" stroke="var(--muted-foreground)" stroke-width="1.2" stroke-dasharray="4 3" opacity="0.6" />
      
      <!-- Poncelet Triangle BCD -->
      <polygon points="60,200 240,130 290,70" fill="var(--pastel-peach-bg, rgba(249,115,22,0.2))" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2" />
      <text x="205" y="150" fill="var(--pastel-peach-foreground, #f97316)" font-size="11" font-weight="bold" font-family="system-ui, sans-serif">C</text>
      
      <line x1="60" y1="200" x2="290" y2="70" stroke="var(--foreground)" stroke-width="2" stroke-dasharray="4 2" />
      <text x="165" y="105" fill="var(--foreground)" font-size="10.5" font-weight="bold" font-family="system-ui, sans-serif">Critical Slip Plane (BC)</text>
      
      <line x1="60" y1="70" x2="135" y2="170" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.2" stroke-dasharray="3 3" />
      <text x="138" y="182" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="10" font-weight="bold" font-family="system-ui, sans-serif">E</text>
      
      <circle cx="60" cy="200" r="2" fill="var(--foreground)" />
      <line x1="135" y1="170" x2="115" y2="45" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.2" stroke-dasharray="3 3" />
      <text x="110" y="40" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="10" font-weight="bold" font-family="system-ui, sans-serif">F</text>
      
      <g transform="translate(210, 195)">
        <rect x="0" y="0" width="220" height="38" fill="var(--secondary)" rx="5" />
        <text x="110" y="16" fill="var(--foreground)" font-size="10.5" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Rebhann's Active Thrust Result:</text>
        <text x="110" y="30" fill="var(--pastel-peach-foreground, #f97316)" font-size="11" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Pa = γ × Area(ΔBCD)</text>
      </g>
    </g>
  </svg>
</div>'''

SVG_SPT_APPARATUS = '''<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Standard Penetration Test (SPT) Setup per IS: 2131</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 260" class="sol-diagram-svg" width="100%" style="max-width:460px;height:auto;display:block;">
    <rect width="460" height="260" fill="var(--card)" rx="8" />
    <g transform="translate(35, 15)">
      <line x1="20" y1="110" x2="380" y2="110" stroke="var(--foreground)" stroke-width="1.8" />
      <text x="380" y="105" fill="var(--muted-foreground)" font-size="9.5" text-anchor="end" font-family="system-ui, sans-serif">Ground Surface (GL)</text>
      
      <line x1="70" y1="110" x2="160" y2="15" stroke="var(--muted-foreground)" stroke-width="2" />
      <line x1="250" y1="110" x2="160" y2="15" stroke="var(--muted-foreground)" stroke-width="2" />
      <circle cx="160" cy="15" r="5" fill="var(--foreground)" />
      
      <circle cx="160" cy="22" r="7" fill="none" stroke="var(--foreground)" stroke-width="1.5" />
      <line x1="160" y1="22" x2="160" y2="50" stroke="var(--foreground)" stroke-width="1.5" />
      
      <rect x="146" y="45" width="28" height="22" fill="var(--pastel-peach-foreground, #f97316)" rx="3" />
      <text x="160" y="60" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">63.5 kg</text>
      <text x="180" y="58" fill="var(--foreground)" font-size="10" font-weight="bold" font-family="system-ui, sans-serif">Hammer</text>
      
      <line x1="135" y1="45" x2="135" y2="85" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.5" />
      <polygon points="135,45 132,52 138,52" fill="var(--pastel-sky-foreground, #0ea5e9)" />
      <polygon points="135,85 132,78 138,78" fill="var(--pastel-sky-foreground, #0ea5e9)" />
      <text x="128" y="68" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="9.5" font-weight="bold" text-anchor="end" font-family="system-ui, sans-serif">750 mm Fall</text>
      
      <rect x="148" y="85" width="24" height="8" fill="var(--foreground)" rx="1" />
      <text x="178" y="92" fill="var(--foreground)" font-size="9.5" font-family="system-ui, sans-serif">Anvil</text>
      
      <line x1="160" y1="93" x2="160" y2="180" stroke="var(--foreground)" stroke-width="3" />
      
      <line x1="138" y1="110" x2="138" y2="225" stroke="var(--muted-foreground)" stroke-width="1.5" stroke-dasharray="4 2" />
      <line x1="182" y1="110" x2="182" y2="225" stroke="var(--muted-foreground)" stroke-width="1.5" stroke-dasharray="4 2" />
      <line x1="138" y1="225" x2="182" y2="225" stroke="var(--muted-foreground)" stroke-width="1.5" stroke-dasharray="4 2" />
      
      <!-- Sampler Drive Intervals -->
      <rect x="150" y="180" width="20" height="18" fill="var(--muted)" stroke="var(--foreground)" stroke-width="1.2" />
      <text x="188" y="193" fill="var(--muted-foreground)" font-size="8.5" font-family="system-ui, sans-serif">150 mm: Seating drive (ignored)</text>
      
      <rect x="150" y="198" width="20" height="18" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.2" />
      <rect x="150" y="216" width="20" height="18" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.2" />
      
      <line x1="175" y1="198" x2="182" y2="198" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.5" />
      <line x1="182" y1="198" x2="182" y2="234" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.5" />
      <line x1="175" y1="234" x2="182" y2="234" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.5" />
      <text x="190" y="219" fill="var(--pastel-peach-foreground, #f97316)" font-size="10" font-weight="bold" font-family="system-ui, sans-serif">N = Sum of last 300 mm blows</text>
      
      <text x="300" y="160" fill="var(--foreground)" font-size="9.5" font-weight="bold" font-family="system-ui, sans-serif">Split-Spoon Sampler:</text>
      <text x="300" y="174" fill="var(--muted-foreground)" font-size="9" font-family="system-ui, sans-serif">• OD = 50.8 mm, ID = 35 mm</text>
      <text x="300" y="188" fill="var(--muted-foreground)" font-size="9" font-family="system-ui, sans-serif">• Total Length = 450 mm</text>
      <text x="300" y="202" fill="var(--muted-foreground)" font-size="9" font-family="system-ui, sans-serif">• Standard: IS: 2131-1981</text>
    </g>
  </svg>
</div>'''

SVG_BORELOG = '''<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Typical Soil Investigation Borelog Layout (IS: 1892)</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 280" class="sol-diagram-svg" width="100%" style="max-width:520px;height:auto;display:block;">
    <rect width="520" height="280" fill="var(--card)" rx="8" />
    <g transform="translate(20, 15)">
      <rect x="0" y="0" width="480" height="32" fill="var(--secondary)" rx="4" />
      <text x="10" y="20" fill="var(--foreground)" font-size="10.5" font-weight="bold" font-family="system-ui, sans-serif">BORELOG: BH-01 | Location: Pier P2 | GL: +100.00 m | Method: Rotary / Wash Boring (IS: 1892)</text>
      
      <g transform="translate(0, 40)">
        <rect x="0" y="0" width="480" height="24" fill="var(--muted)" />
        <text x="25" y="16" fill="var(--foreground)" font-size="9.5" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Depth</text>
        <text x="75" y="16" fill="var(--foreground)" font-size="9.5" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Soil Hatch</text>
        <text x="190" y="16" fill="var(--foreground)" font-size="9.5" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Strata Description (IS Classification)</text>
        <text x="345" y="16" fill="var(--foreground)" font-size="9.5" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">Water Table</text>
        <text x="435" y="16" fill="var(--foreground)" font-size="9.5" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">SPT N (N1)</text>
        
        <line x1="0" y1="24" x2="480" y2="24" stroke="var(--foreground)" stroke-width="1" />
        
        <!-- Layer 1: 0 - 2.5m -->
        <rect x="50" y="24" width="50" height="36" fill="var(--secondary)" opacity="0.6" />
        <text x="25" y="46" fill="var(--foreground)" font-size="9" text-anchor="middle" font-family="system-ui, sans-serif">0.0 - 2.5 m</text>
        <text x="75" y="46" fill="var(--muted-foreground)" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">≡ ≡ ≡</text>
        <text x="120" y="42" fill="var(--foreground)" font-size="9" font-weight="bold" font-family="system-ui, sans-serif">Firm Brown Silty CLAY (CI)</text>
        <text x="120" y="54" fill="var(--muted-foreground)" font-size="8" font-family="system-ui, sans-serif">Medium plasticity, LL=38%, PL=21%</text>
        <text x="435" y="46" fill="var(--foreground)" font-size="9.5" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">6 (8)</text>
        <line x1="0" y1="60" x2="480" y2="60" stroke="var(--muted-foreground)" stroke-width="0.5" />
        
        <!-- Layer 2: 2.5 - 6.0m -->
        <rect x="50" y="60" width="50" height="44" fill="var(--secondary)" opacity="0.4" />
        <text x="25" y="85" fill="var(--foreground)" font-size="9" text-anchor="middle" font-family="system-ui, sans-serif">2.5 - 6.0 m</text>
        <text x="75" y="85" fill="var(--muted-foreground)" font-size="9" text-anchor="middle" font-family="system-ui, sans-serif">∴ ∴ ∴</text>
        <text x="120" y="80" fill="var(--foreground)" font-size="9" font-weight="bold" font-family="system-ui, sans-serif">Medium Dense Grey SAND (SP-SM)</text>
        <text x="120" y="92" fill="var(--muted-foreground)" font-size="8" font-family="system-ui, sans-serif">Sub-angular quartz grains, Dr ≈ 48%</text>
        
        <!-- GWT -->
        <polygon points="345,63 340,69 350,69" fill="var(--pastel-sky-foreground, #0ea5e9)" />
        <line x1="337" y1="71" x2="353" y2="71" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.5" />
        <line x1="340" y1="73" x2="350" y2="73" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1" />
        <text x="345" y="86" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="8.5" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">GWT -2.5m</text>
        
        <text x="435" y="85" fill="var(--foreground)" font-size="9.5" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">18 (19)</text>
        <line x1="0" y1="104" x2="480" y2="104" stroke="var(--muted-foreground)" stroke-width="0.5" />
        
        <!-- Layer 3: 6.0 - 10.0m -->
        <rect x="50" y="104" width="50" height="44" fill="var(--secondary)" opacity="0.5" />
        <text x="25" y="128" fill="var(--foreground)" font-size="9" text-anchor="middle" font-family="system-ui, sans-serif">6.0 - 10.0 m</text>
        <text x="75" y="128" fill="var(--muted-foreground)" font-size="9" text-anchor="middle" font-family="system-ui, sans-serif">o o ∴</text>
        <text x="120" y="123" fill="var(--foreground)" font-size="9" font-weight="bold" font-family="system-ui, sans-serif">Dense Coarse SAND &amp; GRAVEL (GW)</text>
        <text x="120" y="135" fill="var(--muted-foreground)" font-size="8" font-family="system-ui, sans-serif">Compacted stratum, Dr ≈ 76%</text>
        <text x="435" y="128" fill="var(--foreground)" font-size="9.5" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">34 (31)</text>
        <line x1="0" y1="148" x2="480" y2="148" stroke="var(--muted-foreground)" stroke-width="0.5" />
        
        <!-- Layer 4: > 10.0m -->
        <rect x="50" y="148" width="50" height="40" fill="var(--muted)" />
        <text x="25" y="172" fill="var(--foreground)" font-size="9" text-anchor="middle" font-family="system-ui, sans-serif">&gt; 10.0 m</text>
        <text x="75" y="172" fill="var(--foreground)" font-size="9.5" text-anchor="middle" font-family="system-ui, sans-serif">// // //</text>
        <text x="120" y="167" fill="var(--foreground)" font-size="9" font-weight="bold" font-family="system-ui, sans-serif">Sandstone BEDROCK (Competent Rock)</text>
        <text x="120" y="179" fill="var(--muted-foreground)" font-size="8" font-family="system-ui, sans-serif">TCR = 85%, RQD = 72%</text>
        <text x="435" y="172" fill="var(--pastel-peach-foreground, #f97316)" font-size="9.5" font-weight="bold" text-anchor="middle" font-family="system-ui, sans-serif">&gt; 50 (Refusal)</text>
        <line x1="0" y1="188" x2="480" y2="188" stroke="var(--foreground)" stroke-width="1" />
      </g>
      
      <text x="240" y="252" fill="var(--muted-foreground)" font-size="8.5" text-anchor="middle" font-family="system-ui, sans-serif">Standard Subsurface Investigation Borelog Format (IS: 1892-1979)</text>
    </g>
  </svg>
</div>'''
