# -*- coding: utf-8 -*-
"""
High-Definition Editorial Vector SVG Diagrams for Geotechnical Engineering.
Features:
- Vibrant semantic color tokens (water blue, sand gold, concrete slate, bedrock sage, load coral).
- Crisp, necessary, high-yield labels with generous safety margins (zero text clipping).
- True architectural textures (sand stipple, concrete speckles, bedrock hatch).
- 100% theme-aware in both light and dark mode.
"""

def get_diagram_open_caisson():
    return '''<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Cross-Section of Open Caisson (Well Foundation) Components (IS: 3955)</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 415" class="sol-diagram-svg" width="100%" style="max-width:660px;height:auto;display:block;">
    <defs>
      <!-- Concrete Pattern -->
      <pattern id="caisson-concrete" width="14" height="14" patternUnits="userSpaceOnUse">
        <path d="M 0 14 L 14 0" stroke="var(--muted-foreground)" stroke-width="0.6" opacity="0.25" />
        <circle cx="3" cy="3" r="0.6" fill="var(--muted-foreground)" opacity="0.35" />
        <circle cx="10" cy="9" r="0.6" fill="var(--muted-foreground)" opacity="0.35" />
      </pattern>
      <!-- Sand Ballast Pattern -->
      <pattern id="caisson-sand" width="10" height="10" patternUnits="userSpaceOnUse">
        <circle cx="2" cy="2" r="0.75" fill="var(--pastel-sand-foreground, #ca8a04)" opacity="0.5" />
        <circle cx="7" cy="7" r="0.75" fill="var(--pastel-sand-foreground, #ca8a04)" opacity="0.5" />
      </pattern>
      <!-- Bedrock Pattern -->
      <pattern id="caisson-bedrock" width="14" height="14" patternUnits="userSpaceOnUse">
        <path d="M 0 14 L 14 0 M -2 2 L 2 -2 M 12 16 L 16 12" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="0.8" opacity="0.35" />
      </pattern>
      <marker id="caisson-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--pastel-peach-foreground, #f97316)" />
      </marker>
    </defs>

    <!-- River Water Wash between HFL and River Bed -->
    <rect x="110" y="100" width="145" height="125" fill="var(--pastel-sky-bg)" opacity="0.5" rx="2" />
    <rect x="405" y="100" width="145" height="125" fill="var(--pastel-sky-bg)" opacity="0.5" rx="2" />

    <!-- Water Levels -->
    <line x1="85" y1="100" x2="575" y2="100" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.4" stroke-dasharray="5 3" />
    <text x="580" y="104" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="9.5" font-weight="700" font-family="system-ui, sans-serif">▽ H.F.L.</text>

    <line x1="85" y1="225" x2="575" y2="225" stroke="var(--muted-foreground)" stroke-width="1.4" stroke-dasharray="4 2" />
    <text x="580" y="229" fill="var(--muted-foreground)" font-size="9.5" font-weight="700" font-family="system-ui, sans-serif">⏚ River Bed</text>

    <!-- Founding Stratum Bedrock Base -->
    <rect x="110" y="375" width="440" height="28" fill="var(--pastel-sage-bg)" rx="3" />
    <rect x="110" y="375" width="440" height="28" fill="url(#caisson-bedrock)" rx="3" />
    <line x1="85" y1="375" x2="575" y2="375" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="2" stroke-dasharray="6 3" />
    <text x="330" y="394" fill="var(--pastel-sage-foreground, #059669)" font-size="10.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Founding Stratum (Hard Rock / Dense Bed)</text>

    <!-- Central Sinking Shaft (Dredge Hole) -->
    <rect x="290" y="52" width="80" height="268" fill="var(--secondary)" opacity="0.6" />

    <!-- Sand Filling (Ballast) - Warm Golden Sand Color -->
    <rect x="290" y="76" width="80" height="188" fill="var(--pastel-sand-bg)" />
    <rect x="290" y="76" width="80" height="188" fill="url(#caisson-sand)" />

    <!-- Bottom Plug (Tremie Concrete Seal) -->
    <path d="M 290 264 Q 330 246 370 264 L 370 320 L 290 320 Z" fill="var(--pastel-sky-bg)" stroke="var(--foreground)" stroke-width="1.6" />
    <path d="M 290 264 Q 330 246 370 264 L 370 320 L 290 320 Z" fill="url(#caisson-concrete)" />

    <!-- Left Steining Wall -->
    <rect x="255" y="52" width="35" height="268" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.8" />
    <rect x="255" y="52" width="35" height="268" fill="url(#caisson-concrete)" />

    <!-- Right Steining Wall -->
    <rect x="370" y="52" width="35" height="268" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.8" />
    <rect x="370" y="52" width="35" height="268" fill="url(#caisson-concrete)" />

    <!-- Top Plug Concrete Slab -->
    <rect x="290" y="52" width="80" height="24" fill="var(--pastel-sky-bg)" stroke="var(--foreground)" stroke-width="1.5" />
    <rect x="290" y="52" width="80" height="24" fill="url(#caisson-concrete)" />

    <!-- Left Well Curb (Tapered RCC Wedge) -->
    <polygon points="255,320 290,320 255,362" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.8" />
    <polygon points="255,320 290,320 255,362" fill="url(#caisson-concrete)" />

    <!-- Right Well Curb (Tapered RCC Wedge) -->
    <polygon points="405,320 370,320 405,362" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.8" />
    <polygon points="405,320 370,320 405,362" fill="url(#caisson-concrete)" />

    <!-- Left Cutting Edge (Hardened Steel Shoe) -->
    <polygon points="255,362 268,362 255,376" fill="var(--foreground)" stroke="var(--foreground)" stroke-width="1" />

    <!-- Right Cutting Edge (Hardened Steel Shoe) -->
    <polygon points="405,362 392,362 405,376" fill="var(--foreground)" stroke="var(--foreground)" stroke-width="1" />

    <!-- Well Cap (Top RCC Slab) - Subtle Peach Tint -->
    <rect x="240" y="28" width="180" height="24" fill="var(--pastel-peach-bg)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2" rx="3" />
    
    <!-- Superstructure Pier Shaft & Load Q -->
    <rect x="305" y="8" width="50" height="20" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.4" rx="2" />
    <text x="330" y="22" fill="var(--foreground)" font-size="9" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">PIER</text>
    <line x1="330" y1="-2" x2="330" y2="7" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2.6" marker-end="url(#caisson-arrow)" />

    <!-- ==================== LEFT CALLOUTS (Clean & Concise) ==================== -->
    <!-- Pier Load -->
    <line x1="185" y1="18" x2="295" y2="18" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.2" />
    <circle cx="295" cy="18" r="2.5" fill="var(--pastel-peach-foreground, #f97316)" />
    <text x="180" y="16" fill="var(--pastel-peach-foreground, #f97316)" font-size="11" font-weight="800" text-anchor="end" font-family="system-ui, sans-serif">Pier Load (Q)</text>
    <text x="180" y="28" fill="var(--muted-foreground)" font-size="9" text-anchor="end" font-family="system-ui, sans-serif">(Superstructure Load)</text>

    <!-- Steining Wall -->
    <line x1="185" y1="145" x2="225" y2="145" stroke="var(--foreground)" stroke-width="1.2" />
    <line x1="225" y1="145" x2="255" y2="160" stroke="var(--foreground)" stroke-width="1.2" />
    <circle cx="255" cy="160" r="3" fill="var(--primary)" />
    <text x="180" y="142" fill="var(--foreground)" font-size="11" font-weight="800" text-anchor="end" font-family="system-ui, sans-serif">Steining Wall</text>
    <text x="180" y="155" fill="var(--muted-foreground)" font-size="9" text-anchor="end" font-family="system-ui, sans-serif">(Massive RCC Self-Weight)</text>

    <!-- Central Dredge Hole -->
    <line x1="185" y1="195" x2="235" y2="195" stroke="var(--foreground)" stroke-width="1.2" />
    <line x1="235" y1="195" x2="310" y2="195" stroke="var(--foreground)" stroke-width="1.2" />
    <circle cx="310" cy="195" r="3" fill="var(--primary)" />
    <text x="180" y="192" fill="var(--foreground)" font-size="11" font-weight="800" text-anchor="end" font-family="system-ui, sans-serif">Dredge Hole</text>
    <text x="180" y="205" fill="var(--muted-foreground)" font-size="9" text-anchor="end" font-family="system-ui, sans-serif">(Excavation Shaft)</text>

    <!-- Cutting Edge -->
    <line x1="185" y1="362" x2="230" y2="362" stroke="var(--foreground)" stroke-width="1.2" />
    <line x1="230" y1="362" x2="255" y2="368" stroke="var(--foreground)" stroke-width="1.2" />
    <circle cx="255" cy="368" r="3" fill="var(--primary)" />
    <text x="180" y="359" fill="var(--foreground)" font-size="11" font-weight="800" text-anchor="end" font-family="system-ui, sans-serif">Cutting Edge</text>
    <text x="180" y="372" fill="var(--muted-foreground)" font-size="9" text-anchor="end" font-family="system-ui, sans-serif">(Steel Shoe Angle)</text>

    <!-- ==================== RIGHT CALLOUTS (Clean & Concise) ==================== -->
    <!-- Well Cap -->
    <line x1="420" y1="40" x2="470" y2="40" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.2" />
    <circle cx="420" cy="40" r="2.5" fill="var(--pastel-peach-foreground, #f97316)" />
    <text x="475" y="38" fill="var(--pastel-peach-foreground, #f97316)" font-size="11" font-weight="800" font-family="system-ui, sans-serif">Well Cap</text>
    <text x="475" y="50" fill="var(--muted-foreground)" font-size="9" font-family="system-ui, sans-serif">(Top RCC Slab)</text>

    <!-- Top Plug -->
    <line x1="370" y1="64" x2="440" y2="64" stroke="var(--foreground)" stroke-width="1.2" />
    <line x1="440" y1="64" x2="470" y2="72" stroke="var(--foreground)" stroke-width="1.2" />
    <circle cx="370" cy="64" r="3" fill="var(--primary)" />
    <text x="475" y="72" fill="var(--foreground)" font-size="11" font-weight="800" font-family="system-ui, sans-serif">Top Plug</text>
    <text x="475" y="85" fill="var(--muted-foreground)" font-size="9" font-family="system-ui, sans-serif">(Concrete Seal)</text>

    <!-- Sand Filling -->
    <line x1="370" y1="155" x2="435" y2="155" stroke="var(--pastel-sand-foreground, #ca8a04)" stroke-width="1.2" />
    <line x1="435" y1="155" x2="470" y2="155" stroke="var(--pastel-sand-foreground, #ca8a04)" stroke-width="1.2" />
    <circle cx="370" cy="155" r="3" fill="var(--pastel-sand-foreground, #ca8a04)" />
    <text x="475" y="153" fill="var(--pastel-sand-foreground, #ca8a04)" font-size="11" font-weight="800" font-family="system-ui, sans-serif">Sand Filling</text>
    <text x="475" y="166" fill="var(--muted-foreground)" font-size="9" font-family="system-ui, sans-serif">(Ballast &amp; Stability)</text>

    <!-- Bottom Plug -->
    <line x1="370" y1="288" x2="435" y2="288" stroke="var(--foreground)" stroke-width="1.2" />
    <line x1="435" y1="288" x2="470" y2="288" stroke="var(--foreground)" stroke-width="1.2" />
    <circle cx="370" cy="288" r="3" fill="var(--primary)" />
    <text x="475" y="286" fill="var(--foreground)" font-size="11" font-weight="800" font-family="system-ui, sans-serif">Bottom Plug</text>
    <text x="475" y="299" fill="var(--muted-foreground)" font-size="9" font-family="system-ui, sans-serif">(Tremie Concrete Arch)</text>

    <!-- Well Curb -->
    <line x1="405" y1="340" x2="445" y2="340" stroke="var(--foreground)" stroke-width="1.2" />
    <line x1="445" y1="340" x2="470" y2="340" stroke="var(--foreground)" stroke-width="1.2" />
    <circle cx="405" cy="340" r="3" fill="var(--primary)" />
    <text x="475" y="338" fill="var(--foreground)" font-size="11" font-weight="800" font-family="system-ui, sans-serif">Well Curb</text>
    <text x="475" y="351" fill="var(--muted-foreground)" font-size="9" font-family="system-ui, sans-serif">(Tapered RCC Wedge)</text>
  </svg>
</div>'''

def get_diagram_rebhann():
    return '''<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Rebhann's Graphical Construction for Active Thrust (Pa)</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 320" class="sol-diagram-svg" width="100%" style="max-width:620px;height:auto;display:block;">
    <defs>
      <marker id="rebhann-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--pastel-peach-foreground, #f97316)" />
      </marker>
    </defs>

    <!-- Backfill Soil Shading -->
    <polygon points="90,80 500,80 500,240 90,240" fill="var(--pastel-sand-bg)" opacity="0.3" />

    <!-- Retaining Wall Stem AB -->
    <polygon points="60,80 90,80 90,240 50,240" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.8" />
    <line x1="90" y1="80" x2="90" y2="240" stroke="var(--foreground)" stroke-width="2.5" />
    
    <!-- Wall Labels A and B -->
    <circle cx="90" cy="80" r="3" fill="var(--foreground)" />
    <text x="82" y="72" fill="var(--foreground)" font-size="12" font-weight="800" font-family="system-ui, sans-serif">A (Crest)</text>
    <circle cx="90" cy="240" r="3" fill="var(--foreground)" />
    <text x="75" y="256" fill="var(--foreground)" font-size="12" font-weight="800" font-family="system-ui, sans-serif">B (Heel)</text>

    <!-- Ground Surface Line AD -->
    <line x1="90" y1="80" x2="520" y2="80" stroke="var(--foreground)" stroke-width="2" />
    <text x="525" y="84" fill="var(--foreground)" font-size="11" font-weight="700" font-family="system-ui, sans-serif">D (Ground Line)</text>

    <!-- Earth Pressure phi-line BL -->
    <line x1="90" y1="240" x2="490" y2="80" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2" />
    <circle cx="490" cy="80" r="3" fill="var(--pastel-sky-foreground, #0ea5e9)" />
    <text x="495" y="74" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="11" font-weight="800" font-family="system-ui, sans-serif">L (&phi;-line)</text>
    
    <!-- Angle phi arc at B -->
    <path d="M 150 240 A 60 60 0 0 0 144 219" fill="none" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.8" />
    <text x="158" y="228" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="11" font-weight="800" font-family="system-ui, sans-serif">&phi;</text>

    <!-- Semi-circle on BL as diameter -->
    <path d="M 90 240 A 215 215 0 0 1 490 80" fill="none" stroke="var(--muted-foreground)" stroke-width="1.2" stroke-dasharray="4 3" opacity="0.6" />

    <!-- Poncelet Triangle BCD (Radiant Pastel Peach Fill) -->
    <polygon points="90,240 305,154 360,80" fill="var(--pastel-peach-bg)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2.2" />
    <circle cx="305" cy="154" r="3" fill="var(--pastel-peach-foreground, #f97316)" />
    <text x="290" y="152" fill="var(--pastel-peach-foreground, #f97316)" font-size="12" font-weight="800" font-family="system-ui, sans-serif">C</text>

    <!-- Critical Failure Slip Plane BD -->
    <line x1="90" y1="240" x2="360" y2="80" stroke="var(--foreground)" stroke-width="2" stroke-dasharray="5 3" />
    <circle cx="360" cy="80" r="3" fill="var(--foreground)" />
    <text x="360" y="68" fill="var(--foreground)" font-size="11" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">D (Slip Surface)</text>

    <!-- Perpendicular Line FJ to semi-circle -->
    <line x1="360" y1="80" x2="260" y2="28" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.2" stroke-dasharray="3 3" />
    <circle cx="260" cy="28" r="2.5" fill="var(--pastel-sky-foreground, #0ea5e9)" />
    <text x="255" y="22" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="11" font-weight="800" font-family="system-ui, sans-serif">F</text>

    <!-- Tangent Arc from F to C -->
    <path d="M 260 28 A 230 230 0 0 1 305 154" fill="none" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.2" stroke-dasharray="3 3" />

    <!-- Active Thrust Vector Pa -->
    <line x1="90" y1="187" x2="160" y2="160" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2.6" marker-end="url(#rebhann-arrow)" />
    <text x="165" y="155" fill="var(--pastel-peach-foreground, #f97316)" font-size="11.5" font-weight="800" font-family="system-ui, sans-serif">Pa (at H/3)</text>

    <!-- Formula & Intelligence Card -->
    <g transform="translate(350, 205)">
      <rect x="0" y="0" width="245" height="66" fill="var(--card)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.4" rx="6" />
      <text x="14" y="22" fill="var(--foreground)" font-size="10.5" font-weight="800" font-family="system-ui, sans-serif">Rebhann's Active Thrust:</text>
      <text x="14" y="42" fill="var(--pastel-peach-foreground, #f97316)" font-size="13" font-weight="800" font-family="system-ui, sans-serif">Pa = &gamma; &times; Area(&Delta;BCD)</text>
      <text x="14" y="56" fill="var(--muted-foreground)" font-size="9" font-family="system-ui, sans-serif">Inclined at angle &delta; at H/3 above base</text>
    </g>
  </svg>
</div>'''

def get_diagram_shear_curves():
    return '''<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Load-Settlement (q vs s) Curves for Modes of Failure</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 300" class="sol-diagram-svg" width="100%" style="max-width:580px;height:auto;display:block;">
    <defs>
      <marker id="curve-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--foreground)" />
      </marker>
    </defs>

    <!-- Subtle Grid Lines -->
    <line x1="80" y1="190" x2="520" y2="190" stroke="var(--muted-foreground)" stroke-width="0.5" stroke-dasharray="2 4" opacity="0.3" />
    <line x1="80" y1="130" x2="520" y2="130" stroke="var(--muted-foreground)" stroke-width="0.5" stroke-dasharray="2 4" opacity="0.3" />
    <line x1="80" y1="70" x2="520" y2="70" stroke="var(--muted-foreground)" stroke-width="0.5" stroke-dasharray="2 4" opacity="0.3" />

    <!-- Axes -->
    <line x1="80" y1="250" x2="530" y2="250" stroke="var(--foreground)" stroke-width="1.8" marker-end="url(#curve-arrow)" />
    <line x1="80" y1="250" x2="80" y2="25" stroke="var(--foreground)" stroke-width="1.8" marker-end="url(#curve-arrow)" />

    <text x="535" y="254" fill="var(--foreground)" font-size="11" font-weight="700" font-family="system-ui, sans-serif">Settlement s &rarr;</text>
    <text x="75" y="18" fill="var(--foreground)" font-size="11" font-weight="700" text-anchor="end" font-family="system-ui, sans-serif">Load Intensity q &rarr;</text>

    <!-- Curve 1: General Shear Failure (Sharp Peak qu, Abrupt Plunge) -->
    <path d="M 80 250 C 130 170, 180 75, 230 70 C 260 70, 290 140, 340 180" fill="none" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="3" />
    
    <!-- Projection Lines for qu -->
    <line x1="80" y1="70" x2="230" y2="70" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.2" stroke-dasharray="3 3" />
    <line x1="230" y1="70" x2="230" y2="250" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.2" stroke-dasharray="3 3" />
    <circle cx="230" cy="70" r="3.5" fill="var(--pastel-peach-foreground, #f97316)" />
    <text x="72" y="73" fill="var(--pastel-peach-foreground, #f97316)" font-size="11.5" font-weight="800" text-anchor="end" font-family="system-ui, sans-serif">qu</text>
    <text x="230" y="56" fill="var(--pastel-peach-foreground, #f97316)" font-size="10.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Peak (qu)</text>

    <!-- Curve 2: Local Shear Failure (Initial Yield qu1, Plastic Stretch) -->
    <path d="M 80 250 C 150 200, 240 145, 310 140 C 380 135, 430 130, 480 125" fill="none" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2.6" />
    <circle cx="310" cy="140" r="3" fill="var(--pastel-sky-foreground, #0ea5e9)" />
    <text x="310" y="128" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="10" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Yield (qu1)</text>

    <!-- Curve 3: Punching Shear Failure (Continuous Yield, No Peak) -->
    <path d="M 80 250 C 180 235, 300 220, 420 190 C 460 180, 490 170, 520 160" fill="none" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="2.4" stroke-dasharray="5 3" />
    
    <!-- Legend & Labels -->
    <g transform="translate(290, 22)">
      <rect x="0" y="0" width="260" height="82" fill="var(--card)" stroke="var(--secondary)" stroke-width="1.2" rx="6" />
      
      <!-- Item 1 -->
      <line x1="12" y1="18" x2="35" y2="18" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="3" />
      <text x="42" y="21" fill="var(--foreground)" font-size="9.5" font-weight="700" font-family="system-ui, sans-serif">General Shear (Dense, Dr &gt; 70%)</text>
      
      <!-- Item 2 -->
      <line x1="12" y1="42" x2="35" y2="42" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2.6" />
      <text x="42" y="45" fill="var(--foreground)" font-size="9.5" font-weight="700" font-family="system-ui, sans-serif">Local Shear (Medium, 30-70%)</text>
      
      <!-- Item 3 -->
      <line x1="12" y1="64" x2="35" y2="64" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="2.4" stroke-dasharray="4 2" />
      <text x="42" y="67" fill="var(--foreground)" font-size="9.5" font-weight="700" font-family="system-ui, sans-serif">Punching Shear (Loose, Dr &lt; 30%)</text>
    </g>
  </svg>
</div>'''

def get_diagram_shear_modes_3panels():
    return '''<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Modes of Shear Failure &amp; Rupture Surfaces (Terzaghi / Vesic)</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 260" class="sol-diagram-svg" width="100%" style="max-width:760px;height:auto;display:block;">
    <defs>
      <marker id="mode-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--pastel-peach-foreground, #f97316)" />
      </marker>
    </defs>

    <!-- ==================== PANEL 1: GENERAL SHEAR ==================== -->
    <g transform="translate(15, 10)">
      <rect x="0" y="0" width="230" height="235" fill="var(--card)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.4" rx="6" />
      <text x="115" y="24" fill="var(--foreground)" font-size="11.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">General Shear Failure</text>
      <text x="115" y="38" fill="var(--pastel-peach-foreground, #f97316)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Dense Sand (Dr &gt; 70%)</text>
      
      <!-- Ground Line with Heave -->
      <path d="M 10 110 Q 40 92 75 110 L 155 110 Q 190 92 220 110" fill="none" stroke="var(--foreground)" stroke-width="1.6" />
      <text x="42" y="90" fill="var(--pastel-peach-foreground, #f97316)" font-size="8.5" font-weight="800" font-family="system-ui, sans-serif">Heave &uarr;</text>
      <text x="185" y="90" fill="var(--pastel-peach-foreground, #f97316)" font-size="8.5" font-weight="800" font-family="system-ui, sans-serif">&uarr; Heave</text>

      <!-- Footing Block -->
      <rect x="90" y="85" width="50" height="25" fill="var(--pastel-peach-bg)" stroke="var(--foreground)" stroke-width="1.6" rx="2" />
      <text x="115" y="101" fill="var(--foreground)" font-size="9.5" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Footing</text>
      <line x1="115" y1="52" x2="115" y2="82" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2.2" marker-end="url(#mode-arrow)" />

      <!-- Zone I: Elastic Wedge -->
      <polygon points="90,110 140,110 115,135" fill="var(--pastel-peach-bg)" stroke="var(--foreground)" stroke-width="1.2" />
      <text x="115" y="124" fill="var(--foreground)" font-size="8.5" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">I</text>

      <!-- Rupture Surfaces Reaching Ground Surface -->
      <path d="M 115 135 C 75 135, 45 125, 25 110" fill="none" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2" />
      <path d="M 115 135 C 155 135, 185 125, 205 110" fill="none" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2" />
      
      <text x="115" y="165" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Slip surface reaches ground</text>
      <text x="115" y="180" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Pronounced peak; sudden tilting</text>
      <text x="115" y="195" fill="var(--muted-foreground)" font-size="8.5" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Very small failure settlement</text>
    </g>

    <!-- ==================== PANEL 2: LOCAL SHEAR ==================== -->
    <g transform="translate(265, 10)">
      <rect x="0" y="0" width="230" height="235" fill="var(--card)" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.4" rx="6" />
      <text x="115" y="24" fill="var(--foreground)" font-size="11.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Local Shear Failure</text>
      <text x="115" y="38" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Medium Sand (30% - 70%)</text>
      
      <!-- Ground Line (Minor Heave) -->
      <path d="M 10 110 Q 55 104 80 110 L 150 110 Q 175 104 220 110" fill="none" stroke="var(--foreground)" stroke-width="1.6" />
      <text x="45" y="96" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="8.5" font-weight="700" font-family="system-ui, sans-serif">Minor</text>

      <!-- Footing Block -->
      <rect x="90" y="85" width="50" height="25" fill="var(--pastel-sky-bg)" stroke="var(--foreground)" stroke-width="1.6" rx="2" />
      <text x="115" y="101" fill="var(--foreground)" font-size="9.5" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Footing</text>
      <line x1="115" y1="52" x2="115" y2="82" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2.2" marker-end="url(#mode-arrow)" />

      <!-- Zone I: Elastic Wedge -->
      <polygon points="90,110 140,110 115,135" fill="var(--pastel-sky-bg)" stroke="var(--foreground)" stroke-width="1.2" />

      <!-- Slip Surfaces Terminating Inside Soil -->
      <path d="M 115 135 C 85 135, 65 130, 48 122" fill="none" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2" stroke-dasharray="4 2" />
      <path d="M 115 135 C 145 135, 165 130, 182 122" fill="none" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2" stroke-dasharray="4 2" />
      <circle cx="48" cy="122" r="2.5" fill="var(--pastel-sky-foreground, #0ea5e9)" />
      <circle cx="182" cy="122" r="2.5" fill="var(--pastel-sky-foreground, #0ea5e9)" />
      
      <text x="115" y="165" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Slip surfaces end inside soil</text>
      <text x="115" y="180" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">&bull; No distinct peak; gradual yield</text>
      <text x="115" y="195" fill="var(--muted-foreground)" font-size="8.5" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Significant settlement before yield</text>
    </g>

    <!-- ==================== PANEL 3: PUNCHING SHEAR ==================== -->
    <g transform="translate(515, 10)">
      <rect x="0" y="0" width="230" height="235" fill="var(--card)" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="1.4" rx="6" />
      <text x="115" y="24" fill="var(--foreground)" font-size="11.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Punching Shear Failure</text>
      <text x="115" y="38" fill="var(--pastel-lavender-foreground, #a855f7)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Loose Sand (Dr &lt; 30%)</text>
      
      <!-- Ground Line (Zero Heave) -->
      <line x1="10" y1="100" x2="85" y2="100" stroke="var(--foreground)" stroke-width="1.6" />
      <line x1="145" y1="100" x2="220" y2="100" stroke="var(--foreground)" stroke-width="1.6" />
      <text x="115" y="90" fill="var(--muted-foreground)" font-size="8.5" font-weight="600" text-anchor="middle" font-family="system-ui, sans-serif">No Surface Heave</text>

      <!-- Footing Block Penetrating Deep -->
      <rect x="90" y="100" width="50" height="25" fill="var(--pastel-lavender-bg)" stroke="var(--foreground)" stroke-width="1.6" rx="2" />
      <text x="115" y="116" fill="var(--foreground)" font-size="9.5" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Footing</text>
      <line x1="115" y1="58" x2="115" y2="96" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="2.2" marker-end="url(#mode-arrow)" />

      <!-- Vertical Shearing Edges -->
      <line x1="90" y1="125" x2="90" y2="175" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="2" stroke-dasharray="3 2" />
      <line x1="140" y1="125" x2="140" y2="175" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="2" stroke-dasharray="3 2" />

      <text x="115" y="185" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Shearing along vertical edges</text>
      <text x="115" y="200" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Large continuous settlement</text>
      <text x="115" y="215" fill="var(--muted-foreground)" font-size="8.5" text-anchor="middle" font-family="system-ui, sans-serif">&bull; No tilting; soil around undisturbed</text>
    </g>
  </svg>
</div>'''

def get_diagram_strap_footing():
    return '''<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Elevation &amp; Structural Action of Strap (Cantilever) Footing</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 280" class="sol-diagram-svg" width="100%" style="max-width:640px;height:auto;display:block;">
    <defs>
      <marker id="strap-arrow-up" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
        <path d="M 0 9 L 5 0 L 10 9 z" fill="var(--pastel-sage-foreground, #059669)" />
      </marker>
      <marker id="strap-arrow-down" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--foreground)" />
      </marker>
    </defs>

    <!-- Property Line Boundary Limit -->
    <line x1="80" y1="15" x2="80" y2="245" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2" stroke-dasharray="6 3" />
    <text x="75" y="32" fill="var(--pastel-peach-foreground, #f97316)" font-size="10.5" font-weight="800" text-anchor="end" font-family="system-ui, sans-serif">Property Line</text>
    <text x="75" y="46" fill="var(--muted-foreground)" font-size="8.5" text-anchor="end" font-family="system-ui, sans-serif">(Boundary Limit)</text>

    <!-- Ground Line -->
    <line x1="60" y1="95" x2="600" y2="95" stroke="var(--foreground)" stroke-width="1.4" />
    <text x="595" y="88" fill="var(--muted-foreground)" font-size="9" text-anchor="end" font-family="system-ui, sans-serif">Ground Level (G.L.)</text>

    <!-- Exterior Column C1 (Flush with Property Line) -->
    <rect x="80" y="35" width="28" height="95" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.8" />
    <text x="94" y="65" fill="var(--foreground)" font-size="10.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">C1</text>
    <line x1="94" y1="10" x2="94" y2="33" stroke="var(--foreground)" stroke-width="2.2" marker-end="url(#strap-arrow-down)" />
    <text x="94" y="8" fill="var(--foreground)" font-size="10" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">P1</text>

    <!-- Exterior Eccentric Footing -->
    <rect x="80" y="130" width="85" height="32" fill="var(--pastel-peach-bg)" stroke="var(--foreground)" stroke-width="1.8" rx="2" />
    <text x="122" y="150" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Footing 1</text>

    <!-- Interior Column C2 (Concentric) -->
    <rect x="470" y="35" width="30" height="95" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.8" />
    <text x="485" y="65" fill="var(--foreground)" font-size="10.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">C2</text>
    <line x1="485" y1="10" x2="485" y2="33" stroke="var(--foreground)" stroke-width="2.2" marker-end="url(#strap-arrow-down)" />
    <text x="485" y="8" fill="var(--foreground)" font-size="10" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">P2</text>

    <!-- Interior Footing (Larger & Concentric) -->
    <rect x="415" y="130" width="140" height="32" fill="var(--pastel-sky-bg)" stroke="var(--foreground)" stroke-width="1.8" rx="2" />
    <text x="485" y="150" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Footing 2 (Concentric)</text>

    <!-- Rigid Strap (Cantilever) Beam - Prominent Tint -->
    <rect x="80" y="115" width="475" height="26" fill="var(--pastel-sky-bg)" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2.2" rx="3" />
    <text x="290" y="132" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="11" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">RIGID STRAP BEAM</text>

    <!-- Air Gap / No Soil Contact Note -->
    <line x1="170" y1="145" x2="410" y2="145" stroke="var(--muted-foreground)" stroke-width="1" stroke-dasharray="3 3" opacity="0.6" />
    <text x="290" y="162" fill="var(--muted-foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Air Gap / No Soil Reaction on Strap</text>

    <!-- Upward Soil Reactions q1 under Footing 1 (Vibrant Green) -->
    <line x1="95" y1="195" x2="95" y2="165" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="1.8" marker-end="url(#strap-arrow-up)" />
    <line x1="122" y1="195" x2="122" y2="165" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="1.8" marker-end="url(#strap-arrow-up)" />
    <line x1="150" y1="195" x2="150" y2="165" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="1.8" marker-end="url(#strap-arrow-up)" />
    <text x="122" y="210" fill="var(--pastel-sage-foreground, #059669)" font-size="10" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Uniform q1</text>

    <!-- Upward Soil Reactions q2 under Footing 2 -->
    <line x1="435" y1="195" x2="435" y2="165" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="1.8" marker-end="url(#strap-arrow-up)" />
    <line x1="468" y1="195" x2="468" y2="165" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="1.8" marker-end="url(#strap-arrow-up)" />
    <line x1="502" y1="195" x2="502" y2="165" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="1.8" marker-end="url(#strap-arrow-up)" />
    <line x1="535" y1="195" x2="535" y2="165" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="1.8" marker-end="url(#strap-arrow-up)" />
    <text x="485" y="210" fill="var(--pastel-sage-foreground, #059669)" font-size="10" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Uniform q2</text>

    <!-- Structural Action Callout Card -->
    <g transform="translate(130, 222)">
      <rect x="0" y="0" width="380" height="45" fill="var(--card)" stroke="var(--secondary)" stroke-width="1.2" rx="6" />
      <text x="190" y="18" fill="var(--foreground)" font-size="10" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Cantilever Action: Strap Undergoes Hogging Moment</text>
      <text x="190" y="32" fill="var(--muted-foreground)" font-size="9" text-anchor="middle" font-family="system-ui, sans-serif">Main longitudinal tensile reinforcement placed near top face</text>
    </g>
  </svg>
</div>'''

def get_diagram_spt():
    return '''<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Standard Penetration Test (SPT) Setup per IS: 2131 &amp; Drive Sequence</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 370" class="sol-diagram-svg" width="100%" style="max-width:640px;height:auto;display:block;">
    <defs>
      <marker id="spt-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--pastel-peach-foreground, #f97316)" />
      </marker>
    </defs>

    <!-- ==================== LEFT: FIELD RIG ELEVATION ==================== -->
    <!-- Tripod Legs -->
    <line x1="50" y1="180" x2="165" y2="40" stroke="var(--foreground)" stroke-width="2.5" />
    <line x1="280" y1="180" x2="165" y2="40" stroke="var(--foreground)" stroke-width="2.5" />
    <line x1="165" y1="180" x2="165" y2="40" stroke="var(--muted-foreground)" stroke-width="1.4" stroke-dasharray="4 2" />

    <!-- Crown Pulley -->
    <circle cx="165" cy="40" r="12" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="2" />
    <circle cx="165" cy="40" r="3" fill="var(--foreground)" />

    <!-- Hoisting Rope -->
    <path d="M 153 40 L 153 105" stroke="var(--muted-foreground)" stroke-width="1.8" />
    <path d="M 177 40 L 250 140" stroke="var(--muted-foreground)" stroke-width="1.2" stroke-dasharray="2 2" />

    <!-- 63.5 kg Donut Drop Hammer - Vivid Coral -->
    <rect x="135" y="92" width="60" height="24" fill="var(--pastel-peach-bg)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2" rx="3" />
    <text x="165" y="108" fill="var(--pastel-peach-foreground, #f97316)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">63.5 kg</text>

    <!-- Free Fall Height Dimension (750 mm) -->
    <line x1="210" y1="92" x2="210" y2="148" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.5" />
    <line x1="205" y1="92" x2="215" y2="92" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.5" />
    <line x1="205" y1="148" x2="215" y2="148" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.5" />
    <text x="220" y="124" fill="var(--pastel-peach-foreground, #f97316)" font-size="10" font-weight="800" font-family="system-ui, sans-serif">750 mm</text>

    <!-- Anvil & Drive Head -->
    <rect x="145" y="148" width="40" height="12" fill="var(--foreground)" stroke="var(--foreground)" stroke-width="1.4" rx="2" />
    <text x="165" y="157" fill="var(--background)" font-size="7.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">ANVIL</text>

    <!-- Ground Level GL -->
    <line x1="30" y1="180" x2="310" y2="180" stroke="var(--foreground)" stroke-width="2" />
    <text x="35" y="174" fill="var(--foreground)" font-size="9.5" font-weight="700" font-family="system-ui, sans-serif">Ground Level (&plusmn;0.00)</text>

    <!-- Casing Pipe -->
    <rect x="147" y="180" width="36" height="105" fill="var(--pastel-sky-bg)" opacity="0.4" stroke="var(--foreground)" stroke-width="1.4" />
    <text x="135" y="235" fill="var(--muted-foreground)" font-size="8.5" text-anchor="end" font-family="system-ui, sans-serif">Casing</text>

    <!-- Drill Rods -->
    <line x1="165" y1="160" x2="165" y2="285" stroke="var(--foreground)" stroke-width="3" />

    <!-- Split Spoon Sampler at Borehole Base -->
    <rect x="153" y="285" width="24" height="60" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.6" />
    <polygon points="153,345 165,360 177,345" fill="var(--foreground)" />
    <text x="165" y="320" fill="var(--foreground)" font-size="8" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">IS: 2131</text>

    <!-- ==================== RIGHT: PENETRATION SEQUENCE INSET ==================== -->
    <g transform="translate(340, 25)">
      <rect x="0" y="0" width="280" height="320" fill="var(--card)" stroke="var(--secondary)" stroke-width="1.4" rx="8" />
      
      <text x="140" y="24" fill="var(--foreground)" font-size="11.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Split-Spoon Drive Sequence (450 mm)</text>
      <text x="140" y="38" fill="var(--muted-foreground)" font-size="9" text-anchor="middle" font-family="system-ui, sans-serif">Penetration divided into three 150 mm stages:</text>

      <!-- Stage 1: Seating Drive (0 - 150 mm) -->
      <g transform="translate(18, 52)">
        <rect x="0" y="0" width="45" height="42" fill="var(--secondary)" stroke="var(--muted-foreground)" stroke-width="1.2" rx="3" />
        <text x="22" y="25" fill="var(--muted-foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">150mm</text>
        <text x="55" y="17" fill="var(--foreground)" font-size="10" font-weight="700" font-family="system-ui, sans-serif">0 - 150 mm (Seating Drive)</text>
        <text x="55" y="31" fill="var(--muted-foreground)" font-size="9" font-weight="700" font-family="system-ui, sans-serif">&bull; DISCARDED (Disturbed soil)</text>
      </g>

      <!-- Stage 2: First Test Drive (150 - 300 mm) -->
      <g transform="translate(18, 102)">
        <rect x="0" y="0" width="45" height="42" fill="var(--pastel-sky-bg)" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.6" rx="3" />
        <text x="22" y="26" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="10" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">N1</text>
        <text x="55" y="17" fill="var(--foreground)" font-size="10" font-weight="700" font-family="system-ui, sans-serif">150 - 300 mm (Test Drive 1)</text>
        <text x="55" y="31" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="9" font-weight="700" font-family="system-ui, sans-serif">&bull; Record blow count = N1</text>
      </g>

      <!-- Stage 3: Second Test Drive (300 - 450 mm) -->
      <g transform="translate(18, 152)">
        <rect x="0" y="0" width="45" height="42" fill="var(--pastel-peach-bg)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.6" rx="3" />
        <text x="22" y="26" fill="var(--pastel-peach-foreground, #f97316)" font-size="10" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">N2</text>
        <text x="55" y="17" fill="var(--foreground)" font-size="10" font-weight="700" font-family="system-ui, sans-serif">300 - 450 mm (Test Drive 2)</text>
        <text x="55" y="31" fill="var(--pastel-peach-foreground, #f97316)" font-size="9" font-weight="700" font-family="system-ui, sans-serif">&bull; Record blow count = N2</text>
      </g>

      <!-- SPT N Formula Badge -->
      <rect x="15" y="206" width="250" height="34" fill="var(--pastel-peach-bg)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.5" rx="5" />
      <text x="140" y="227" fill="var(--pastel-peach-foreground, #f97316)" font-size="11.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">SPT Blow Count N = N1 + N2</text>

      <!-- Corrections Summary -->
      <text x="15" y="258" fill="var(--foreground)" font-size="9.5" font-weight="800" font-family="system-ui, sans-serif">Standard Corrections:</text>
      <text x="15" y="274" fill="var(--muted-foreground)" font-size="8.5" font-family="system-ui, sans-serif">1. Overburden: N' = CN &times; N &nbsp;(CN = 350 / (&sigma;' + 70))</text>
      <text x="15" y="290" fill="var(--muted-foreground)" font-size="8.5" font-family="system-ui, sans-serif">2. Dilatancy (Fine Sand, N'&gt;15): N'' = 15 + 0.5(N' - 15)</text>
    </g>
  </svg>
</div>'''

def get_diagram_borelog():
    return '''<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Typical Soil Investigation Borelog Layout (IS: 1892)</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 330" class="sol-diagram-svg" width="100%" style="max-width:660px;height:auto;display:block;">
    <defs>
      <!-- Clay Hatch Pattern -->
      <pattern id="bore-clay" width="18" height="10" patternUnits="userSpaceOnUse">
        <line x1="0" y1="5" x2="18" y2="5" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="0.8" stroke-dasharray="6 3" />
      </pattern>
      <!-- Sand Stipple Pattern -->
      <pattern id="bore-sand" width="10" height="10" patternUnits="userSpaceOnUse">
        <circle cx="2" cy="2" r="0.7" fill="var(--pastel-sand-foreground, #ca8a04)" opacity="0.6" />
        <circle cx="7" cy="7" r="0.7" fill="var(--pastel-sand-foreground, #ca8a04)" opacity="0.6" />
      </pattern>
      <!-- Gravel Pattern -->
      <pattern id="bore-gravel" width="20" height="16" patternUnits="userSpaceOnUse">
        <circle cx="5" cy="5" r="2.2" fill="none" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="0.8" />
        <circle cx="15" cy="11" r="2.5" fill="none" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="0.8" />
      </pattern>
      <!-- Rock Hatch Pattern -->
      <pattern id="bore-rock" width="14" height="14" patternUnits="userSpaceOnUse">
        <line x1="0" y1="14" x2="14" y2="0" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="1.2" opacity="0.5" />
      </pattern>
    </defs>

    <!-- Header Information Bar -->
    <rect x="20" y="15" width="620" height="32" fill="var(--secondary)" stroke="var(--card)" stroke-width="1" rx="4" />
    <text x="35" y="35" fill="var(--foreground)" font-size="10.5" font-weight="800" font-family="system-ui, sans-serif">Borehole: BH-01</text>
    <text x="180" y="35" fill="var(--foreground)" font-size="10" font-family="system-ui, sans-serif">Location: Pier P-2</text>
    <text x="310" y="35" fill="var(--foreground)" font-size="10" font-family="system-ui, sans-serif">G.L.: +104.50 m</text>
    <text x="440" y="35" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="10" font-weight="800" font-family="system-ui, sans-serif">GWT: -2.50 m</text>
    <text x="555" y="35" fill="var(--muted-foreground)" font-size="9" font-family="system-ui, sans-serif">IS: 1892</text>

    <!-- Table Header Columns -->
    <g transform="translate(20, 52)">
      <rect x="0" y="0" width="620" height="24" fill="var(--card)" stroke="var(--foreground)" stroke-width="1" />
      <text x="35" y="16" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Depth</text>
      <text x="105" y="16" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Strata</text>
      <text x="260" y="16" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Soil Classification &amp; Parameters</text>
      <text x="490" y="16" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">SPT Blow Count N</text>
      <text x="585" y="16" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Sample</text>
      
      <!-- Vertical Dividing Lines -->
      <line x1="70" y1="0" x2="70" y2="225" stroke="var(--foreground)" stroke-width="1" />
      <line x1="140" y1="0" x2="140" y2="225" stroke="var(--foreground)" stroke-width="1" />
      <line x1="420" y1="0" x2="420" y2="225" stroke="var(--foreground)" stroke-width="1" />
      <line x1="550" y1="0" x2="550" y2="225" stroke="var(--foreground)" stroke-width="1" />

      <!-- Layer 1: 0.0 - 2.5 m (Silty Clay - Soft Lavender) -->
      <rect x="70" y="24" width="70" height="48" fill="var(--pastel-lavender-bg)" />
      <rect x="70" y="24" width="70" height="48" fill="url(#bore-clay)" />
      <text x="35" y="52" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">0 - 2.5 m</text>
      <text x="155" y="44" fill="var(--foreground)" font-size="10" font-weight="800" font-family="system-ui, sans-serif">Firm Brown Silty CLAY (CI)</text>
      <text x="155" y="58" fill="var(--muted-foreground)" font-size="8.5" font-family="system-ui, sans-serif">LL = 38%, PL = 21%, cu = 45 kPa</text>
      
      <!-- SPT Bar for Layer 1 -->
      <rect x="435" y="38" width="24" height="18" fill="var(--pastel-sky-foreground, #0ea5e9)" rx="2" />
      <text x="470" y="51" fill="var(--foreground)" font-size="10" font-weight="800" font-family="system-ui, sans-serif">N = 6</text>
      <text x="585" y="51" fill="var(--muted-foreground)" font-size="9" text-anchor="middle" font-family="system-ui, sans-serif">U1</text>
      <line x1="0" y1="72" x2="620" y2="72" stroke="var(--foreground)" stroke-width="0.8" />

      <!-- Layer 2: 2.5 - 6.0 m (Sand - Warm Gold) -->
      <rect x="70" y="72" width="70" height="52" fill="var(--pastel-sand-bg)" />
      <rect x="70" y="72" width="70" height="52" fill="url(#bore-sand)" />
      <text x="35" y="102" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">2.5 - 6.0 m</text>
      <text x="155" y="93" fill="var(--foreground)" font-size="10" font-weight="800" font-family="system-ui, sans-serif">Medium Dense Grey SAND (SP-SM)</text>
      <text x="155" y="107" fill="var(--muted-foreground)" font-size="8.5" font-family="system-ui, sans-serif">Dr &asymp; 48%, &phi; = 32&deg;</text>
      
      <!-- Water Table Marker at -2.5m -->
      <polygon points="345,74 340,82 350,82" fill="var(--pastel-sky-foreground, #0ea5e9)" />
      <line x1="335" y1="84" x2="355" y2="84" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.8" />
      <line x1="338" y1="87" x2="352" y2="87" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.2" />
      <text x="362" y="83" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="8.5" font-weight="800" font-family="system-ui, sans-serif">GWT -2.5m</text>

      <!-- SPT Bar for Layer 2 -->
      <rect x="435" y="89" width="72" height="18" fill="var(--pastel-sky-foreground, #0ea5e9)" rx="2" />
      <text x="515" y="102" fill="var(--foreground)" font-size="10" font-weight="800" font-family="system-ui, sans-serif">N = 18</text>
      <text x="585" y="102" fill="var(--muted-foreground)" font-size="9" text-anchor="middle" font-family="system-ui, sans-serif">D1</text>
      <line x1="0" y1="124" x2="620" y2="124" stroke="var(--foreground)" stroke-width="0.8" />

      <!-- Layer 3: 6.0 - 10.0 m (Gravel & Sand - Warm Peach) -->
      <rect x="70" y="124" width="70" height="52" fill="var(--pastel-peach-bg)" />
      <rect x="70" y="124" width="70" height="52" fill="url(#bore-gravel)" />
      <text x="35" y="154" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">6 - 10 m</text>
      <text x="155" y="145" fill="var(--foreground)" font-size="10" font-weight="800" font-family="system-ui, sans-serif">Dense SAND &amp; GRAVEL (GW)</text>
      <text x="155" y="159" fill="var(--muted-foreground)" font-size="8.5" font-family="system-ui, sans-serif">Compacted, Dr &asymp; 76%, &phi; = 38&deg;</text>
      
      <!-- SPT Bar for Layer 3 -->
      <rect x="435" y="141" width="102" height="18" fill="var(--pastel-peach-foreground, #f97316)" rx="2" />
      <text x="515" y="154" fill="var(--foreground)" font-size="10" font-weight="800" font-family="system-ui, sans-serif">N = 34</text>
      <text x="585" y="154" fill="var(--muted-foreground)" font-size="9" text-anchor="middle" font-family="system-ui, sans-serif">D2</text>
      <line x1="0" y1="176" x2="620" y2="176" stroke="var(--foreground)" stroke-width="0.8" />

      <!-- Layer 4: > 10.0 m (Sandstone Bedrock - Sage Green) -->
      <rect x="70" y="176" width="70" height="49" fill="var(--pastel-sage-bg)" />
      <rect x="70" y="176" width="70" height="49" fill="url(#bore-rock)" />
      <text x="35" y="204" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">&gt; 10 m</text>
      <text x="155" y="196" fill="var(--pastel-sage-foreground, #059669)" font-size="10" font-weight="800" font-family="system-ui, sans-serif">Sandstone BEDROCK</text>
      <text x="155" y="210" fill="var(--muted-foreground)" font-size="8.5" font-family="system-ui, sans-serif">TCR = 85%, RQD = 72% (Sound Rock)</text>
      
      <!-- SPT Refusal Bar -->
      <rect x="435" y="192" width="112" height="18" fill="var(--pastel-peach-foreground, #f97316)" rx="2" />
      <text x="445" y="205" fill="var(--primary-foreground, #ffffff)" font-size="9" font-weight="800" font-family="system-ui, sans-serif">&gt; 50 (Refusal)</text>
      <text x="585" y="205" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">C1</text>
      <line x1="0" y1="225" x2="620" y2="225" stroke="var(--foreground)" stroke-width="1.2" />
    </g>

    <!-- Outer Table Border -->
    <rect x="20" y="52" width="620" height="225" fill="none" stroke="var(--foreground)" stroke-width="1.4" rx="2" />
  </svg>
</div>'''

print("Updated HD colorful diagram definitions loaded.")
