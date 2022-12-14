import jinja2

TEMPLATE="""
S : 'a' L 'a' L 'a' D 'u' L 'u' L 'u' # R01 (1 3 5 7 9)
  | 'a' L 'a' L 'u' D 'u' L 'u' L 'a' # R02 (1 3 5 7 9)
  | 'a' L 'a' L 'g' D 'u' L 'u' L 'c' # R03 (1 3 5 7 9)
  | 'a' L 'a' L 'c' D 'u' L 'u' L 'g' # R04 (1 3 5 7 9)
  | 'a' L 'u' L 'a' D 'u' L 'a' L 'u' # R05 (1 3 5 7 9)
  | 'a' L 'u' L 'u' D 'u' L 'a' L 'a' # R06 (1 3 5 7 9)
  | 'a' L 'u' L 'g' D 'u' L 'a' L 'c' # R07 (1 3 5 7 9)
  | 'a' L 'u' L 'c' D 'u' L 'a' L 'g' # R08 (1 3 5 7 9)
  | 'a' L 'g' L 'a' D 'u' L 'c' L 'u' # R09 (1 3 5 7 9)
  | 'a' L 'g' L 'u' D 'u' L 'c' L 'a' # R10 (1 3 5 7 9)
  | 'a' L 'g' L 'g' D 'u' L 'c' L 'c' # R11 (1 3 5 7 9)
  | 'a' L 'g' L 'c' D 'u' L 'c' L 'g' # R12 (1 3 5 7 9)
  | 'a' L 'c' L 'a' D 'u' L 'g' L 'u' # R13 (1 3 5 7 9)
  | 'a' L 'c' L 'u' D 'u' L 'g' L 'a' # R14 (1 3 5 7 9)
  | 'a' L 'c' L 'g' D 'u' L 'g' L 'c' # R15 (1 3 5 7 9)
  | 'a' L 'c' L 'c' D 'u' L 'g' L 'g' # R16 (1 3 5 7 9)
  | 'u' L 'a' L 'a' D 'a' L 'u' L 'u' # R17 (1 3 5 7 9)
  | 'u' L 'a' L 'u' D 'a' L 'u' L 'a' # R18 (1 3 5 7 9)
  | 'u' L 'a' L 'g' D 'a' L 'u' L 'c' # R19 (1 3 5 7 9)
  | 'u' L 'a' L 'c' D 'a' L 'u' L 'g' # R20 (1 3 5 7 9)
  | 'u' L 'u' L 'a' D 'a' L 'a' L 'u' # R21 (1 3 5 7 9)
  | 'u' L 'u' L 'u' D 'a' L 'a' L 'a' # R22 (1 3 5 7 9)
  | 'u' L 'u' L 'g' D 'a' L 'a' L 'c' # R23 (1 3 5 7 9)
  | 'u' L 'u' L 'c' D 'a' L 'a' L 'g' # R24 (1 3 5 7 9)
  | 'u' L 'g' L 'a' D 'a' L 'c' L 'u' # R25 (1 3 5 7 9)
  | 'u' L 'g' L 'u' D 'a' L 'c' L 'a' # R26 (1 3 5 7 9)
  | 'u' L 'g' L 'g' D 'a' L 'c' L 'c' # R27 (1 3 5 7 9)
  | 'u' L 'g' L 'c' D 'a' L 'c' L 'g' # R28 (1 3 5 7 9)
  | 'u' L 'c' L 'a' D 'a' L 'g' L 'u' # R29 (1 3 5 7 9)
  | 'u' L 'c' L 'u' D 'a' L 'g' L 'a' # R30 (1 3 5 7 9)
  | 'u' L 'c' L 'g' D 'a' L 'g' L 'c' # R31 (1 3 5 7 9)
  | 'u' L 'c' L 'c' D 'a' L 'g' L 'g' # R32 (1 3 5 7 9) 
  | 'g' L 'a' L 'a' D 'c' L 'u' L 'u' # R33 (1 3 5 7 9)
  | 'g' L 'a' L 'u' D 'c' L 'u' L 'a' # R34 (1 3 5 7 9)
  | 'g' L 'a' L 'g' D 'c' L 'u' L 'c' # R35 (1 3 5 7 9)
  | 'g' L 'a' L 'c' D 'c' L 'u' L 'g' # R36 (1 3 5 7 9)
  | 'g' L 'u' L 'a' D 'c' L 'a' L 'u' # R37 (1 3 5 7 9)
  | 'g' L 'u' L 'u' D 'c' L 'a' L 'a' # R38 (1 3 5 7 9)
  | 'g' L 'u' L 'g' D 'c' L 'a' L 'c' # R39 (1 3 5 7 9)
  | 'g' L 'u' L 'c' D 'c' L 'a' L 'g' # R40 (1 3 5 7 9)
  | 'g' L 'g' L 'a' D 'c' L 'c' L 'u' # R41 (1 3 5 7 9)
  | 'g' L 'g' L 'u' D 'c' L 'c' L 'a' # R42 (1 3 5 7 9)
  | 'g' L 'g' L 'g' D 'c' L 'c' L 'c' # R43 (1 3 5 7 9)
  | 'g' L 'g' L 'c' D 'c' L 'c' L 'g' # R44 (1 3 5 7 9)
  | 'g' L 'c' L 'a' D 'c' L 'g' L 'u' # R45 (1 3 5 7 9)
  | 'g' L 'c' L 'u' D 'c' L 'g' L 'a' # R46 (1 3 5 7 9)
  | 'g' L 'c' L 'g' D 'c' L 'g' L 'c' # R47 (1 3 5 7 9) 
  | 'g' L 'c' L 'c' D 'c' L 'g' L 'g' # R48 (1 3 5 7 9)
  | 'c' L 'a' L 'a' D 'g' L 'u' L 'u' # R49 (1 3 5 7 9)
  | 'c' L 'a' L 'u' D 'g' L 'u' L 'a' # R50 (1 3 5 7 9)
  | 'c' L 'a' L 'g' D 'g' L 'u' L 'c' # R51 (1 3 5 7 9) 
  | 'c' L 'a' L 'c' D 'g' L 'u' L 'g' # R52 (1 3 5 7 9)
  | 'c' L 'u' L 'a' D 'g' L 'a' L 'u' # R53 (1 3 5 7 9)
  | 'c' L 'u' L 'u' D 'g' L 'a' L 'a' # R54 (1 3 5 7 9)
  | 'c' L 'u' L 'g' D 'g' L 'a' L 'c' # R55 (1 3 5 7 9)
  | 'c' L 'u' L 'c' D 'g' L 'a' L 'g' # R56 (1 3 5 7 9)
  | 'c' L 'g' L 'a' D 'g' L 'c' L 'u' # R57 (1 3 5 7 9)
  | 'c' L 'g' L 'u' D 'g' L 'c' L 'a' # R58 (1 3 5 7 9)
  | 'c' L 'g' L 'g' D 'g' L 'c' L 'c' # R59 (1 3 5 7 9)
  | 'c' L 'g' L 'c' D 'g' L 'c' L 'g' # R60 (1 3 5 7 9)
  | 'c' L 'c' L 'a' D 'g' L 'g' L 'u' # R61 (1 3 5 7 9)
  | 'c' L 'c' L 'u' D 'g' L 'g' L 'a' # R62 (1 3 5 7 9)
  | 'c' L 'c' L 'g' D 'g' L 'g' L 'c' # R63 (1 3 5 7 9)
  | 'c' L 'c' L 'c' D 'g' L 'g' L 'g' # R64 (1 3 5 7 9)
 {%if allow_ug%}
  | 'a' L 'a' L 'g' D 'u' L 'u' L 'u' # R65 (1 3 5 7 9)
  | 'a' L 'a' L 'u' D 'u' L 'u' L 'g' # R66 (1 3 5 7 9)
  | 'a' L 'u' L 'g' D 'u' L 'a' L 'u' # R67 (1 3 5 7 9)
  | 'a' L 'u' L 'u' D 'u' L 'a' L 'g' # R68 (1 3 5 7 9)
  | 'a' L 'g' L 'g' D 'u' L 'c' L 'u' # R69 (1 3 5 7 9)
  | 'a' L 'g' L 'u' D 'u' L 'c' L 'g' # R70 (1 3 5 7 9)
  | 'a' L 'c' L 'g' D 'u' L 'g' L 'u' # R71 (1 3 5 7 9)
  | 'a' L 'c' L 'u' D 'u' L 'g' L 'g' # R72 (1 3 5 7 9)
  | 'a' L 'g' L 'a' D 'u' L 'u' L 'u' # R73 (1 3 5 7 9)
  | 'a' L 'g' L 'u' D 'u' L 'u' L 'a' # R74 (1 3 5 7 9)
  | 'a' L 'g' L 'g' D 'u' L 'u' L 'c' # R75 (1 3 5 7 9)
  | 'a' L 'g' L 'c' D 'u' L 'u' L 'g' # R76 (1 3 5 7 9)
  | 'a' L 'g' L 'g' D 'u' L 'u' L 'u' # R77 (1 3 5 7 9)
  | 'a' L 'g' L 'u' D 'u' L 'u' L 'g' # R78 (1 3 5 7 9)
  | 'a' L 'u' L 'a' D 'u' L 'g' L 'u' # R79 (1 3 5 7 9)
  | 'a' L 'u' L 'u' D 'u' L 'g' L 'a' # R80 (1 3 5 7 9)
  | 'a' L 'u' L 'g' D 'u' L 'g' L 'c' # R81 (1 3 5 7 9)
  | 'a' L 'u' L 'c' D 'u' L 'g' L 'g' # R82 (1 3 5 7 9)
  | 'a' L 'u' L 'g' D 'u' L 'g' L 'u' # R83 (1 3 5 7 9)
  | 'a' L 'u' L 'u' D 'u' L 'g' L 'g' # R84 (1 3 5 7 9)
  | 'u' L 'a' L 'g' D 'a' L 'u' L 'u' # R85 (1 3 5 7 9)
  | 'u' L 'a' L 'u' D 'a' L 'u' L 'g' # R86 (1 3 5 7 9)
  | 'u' L 'u' L 'g' D 'a' L 'a' L 'u' # R87 (1 3 5 7 9)
  | 'u' L 'u' L 'u' D 'a' L 'a' L 'g' # R88 (1 3 5 7 9)
  | 'u' L 'g' L 'g' D 'a' L 'c' L 'u' # R89 (1 3 5 7 9)
  | 'u' L 'g' L 'u' D 'a' L 'c' L 'g' # R90 (1 3 5 7 9)
  | 'u' L 'c' L 'g' D 'a' L 'g' L 'u' # R91 (1 3 5 7 9)
  | 'u' L 'c' L 'u' D 'a' L 'g' L 'g' # R92 (1 3 5 7 9)
  | 'u' L 'g' L 'a' D 'a' L 'u' L 'u' # R93 (1 3 5 7 9)
  | 'u' L 'g' L 'u' D 'a' L 'u' L 'a' # R94 (1 3 5 7 9)
  | 'u' L 'g' L 'g' D 'a' L 'u' L 'c' # R95 (1 3 5 7 9)
  | 'u' L 'g' L 'c' D 'a' L 'u' L 'g' # R96 (1 3 5 7 9)
  | 'u' L 'g' L 'g' D 'a' L 'u' L 'u' # R97 (1 3 5 7 9)
  | 'u' L 'g' L 'u' D 'a' L 'u' L 'g' # R98 (1 3 5 7 9)
  | 'u' L 'u' L 'a' D 'a' L 'g' L 'u' # R99 (1 3 5 7 9)
  | 'u' L 'u' L 'u' D 'a' L 'g' L 'a' # R100 (1 3 5 7 9)
  | 'u' L 'u' L 'g' D 'a' L 'g' L 'c' # R101 (1 3 5 7 9)
  | 'u' L 'u' L 'c' D 'a' L 'g' L 'g' # R102 (1 3 5 7 9)
  | 'u' L 'u' L 'g' D 'a' L 'g' L 'u' # R103 (1 3 5 7 9)
  | 'u' L 'u' L 'u' D 'a' L 'g' L 'g' # R104 (1 3 5 7 9)
  | 'g' L 'a' L 'g' D 'c' L 'u' L 'u' # R105 (1 3 5 7 9)
  | 'g' L 'a' L 'u' D 'c' L 'u' L 'g' # R106 (1 3 5 7 9)
  | 'g' L 'u' L 'g' D 'c' L 'a' L 'u' # R107 (1 3 5 7 9)
  | 'g' L 'u' L 'u' D 'c' L 'a' L 'g' # R108 (1 3 5 7 9)
  | 'g' L 'g' L 'g' D 'c' L 'c' L 'u' # R109 (1 3 5 7 9)
  | 'g' L 'g' L 'u' D 'c' L 'c' L 'g' # R110 (1 3 5 7 9)
  | 'g' L 'c' L 'g' D 'c' L 'g' L 'u' # R111 (1 3 5 7 9)
  | 'g' L 'c' L 'u' D 'c' L 'g' L 'g' # R112 (1 3 5 7 9)
  | 'g' L 'g' L 'a' D 'c' L 'u' L 'u' # R113 (1 3 5 7 9)
  | 'g' L 'g' L 'u' D 'c' L 'u' L 'a' # R114 (1 3 5 7 9)
  | 'g' L 'g' L 'g' D 'c' L 'u' L 'c' # R115 (1 3 5 7 9) 
  | 'g' L 'g' L 'c' D 'c' L 'u' L 'g' # R116 (1 3 5 7 9)
  | 'g' L 'g' L 'g' D 'c' L 'u' L 'u' # R117 (1 3 5 7 9)
  | 'g' L 'g' L 'u' D 'c' L 'u' L 'g' # R118 (1 3 5 7 9)
  | 'g' L 'u' L 'a' D 'c' L 'g' L 'u' # R119 (1 3 5 7 9)
  | 'g' L 'u' L 'u' D 'c' L 'g' L 'a' # R120 (1 3 5 7 9)
  | 'g' L 'u' L 'g' D 'c' L 'g' L 'c' # R121 (1 3 5 7 9)
  | 'g' L 'u' L 'c' D 'c' L 'g' L 'g' # R122 (1 3 5 7 9)
  | 'g' L 'u' L 'g' D 'c' L 'g' L 'u' # R123 (1 3 5 7 9)
  | 'g' L 'u' L 'u' D 'c' L 'g' L 'g' # R124 (1 3 5 7 9)
  | 'c' L 'a' L 'g' D 'g' L 'u' L 'u' # R125 (1 3 5 7 9)
  | 'c' L 'a' L 'u' D 'g' L 'u' L 'g' # R126 (1 3 5 7 9)
  | 'c' L 'u' L 'g' D 'g' L 'a' L 'u' # R127 (1 3 5 7 9)
  | 'c' L 'u' L 'u' D 'g' L 'a' L 'g' # R128 (1 3 5 7 9)
  | 'c' L 'g' L 'g' D 'g' L 'c' L 'u' # R129 (1 3 5 7 9)
  | 'c' L 'g' L 'u' D 'g' L 'c' L 'g' # R130 (1 3 5 7 9)
  | 'c' L 'c' L 'g' D 'g' L 'g' L 'u' # R131 (1 3 5 7 9)
  | 'c' L 'c' L 'u' D 'g' L 'g' L 'g' # R132 (1 3 5 7 9)
  | 'c' L 'g' L 'a' D 'g' L 'u' L 'u' # R133 (1 3 5 7 9)
  | 'c' L 'g' L 'u' D 'g' L 'u' L 'a' # R134 (1 3 5 7 9)
  | 'c' L 'g' L 'g' D 'g' L 'u' L 'c' # R135 (1 3 5 7 9)
  | 'c' L 'g' L 'c' D 'g' L 'u' L 'g' # R136 (1 3 5 7 9)
  | 'c' L 'g' L 'g' D 'g' L 'u' L 'u' # R137 (1 3 5 7 9)
  | 'c' L 'g' L 'u' D 'g' L 'u' L 'g' # R138 (1 3 5 7 9)
  | 'c' L 'u' L 'a' D 'g' L 'g' L 'u' # R139 (1 3 5 7 9)
  | 'c' L 'u' L 'u' D 'g' L 'g' L 'a' # R140 (1 3 5 7 9)
  | 'c' L 'u' L 'g' D 'g' L 'g' L 'c' # R141 (1 3 5 7 9)
  | 'c' L 'u' L 'c' D 'g' L 'g' L 'g' # R142 (1 3 5 7 9)
  | 'c' L 'u' L 'g' D 'g' L 'g' L 'u' # R143 (1 3 5 7 9)
  | 'c' L 'u' L 'u' D 'g' L 'g' L 'g' # R144 (1 3 5 7 9)
  | 'g' L 'a' L 'a' D 'u' L 'u' L 'u' # R145 (1 3 5 7 9)
  | 'g' L 'a' L 'u' D 'u' L 'u' L 'a' # R146 (1 3 5 7 9)
  | 'g' L 'a' L 'g' D 'u' L 'u' L 'c' # R147 (1 3 5 7 9)
  | 'g' L 'a' L 'c' D 'u' L 'u' L 'g' # R148 (1 3 5 7 9)
  | 'g' L 'a' L 'g' D 'u' L 'u' L 'u' # R149 (1 3 5 7 9)
  | 'g' L 'a' L 'u' D 'u' L 'u' L 'g' # R150 (1 3 5 7 9)
  | 'g' L 'u' L 'a' D 'u' L 'a' L 'u' # R151 (1 3 5 7 9)
  | 'g' L 'u' L 'u' D 'u' L 'a' L 'a' # R152 (1 3 5 7 9)
  | 'g' L 'u' L 'g' D 'u' L 'a' L 'c' # R153 (1 3 5 7 9)
  | 'g' L 'u' L 'c' D 'u' L 'a' L 'g' # R154 (1 3 5 7 9)
  | 'g' L 'u' L 'g' D 'u' L 'a' L 'u' # R155 (1 3 5 7 9)
  | 'g' L 'u' L 'u' D 'u' L 'a' L 'g' # R156 (1 3 5 7 9)
  | 'g' L 'g' L 'a' D 'u' L 'c' L 'u' # R157 (1 3 5 7 9)
  | 'g' L 'g' L 'u' D 'u' L 'c' L 'a' # R158 (1 3 5 7 9)
  | 'g' L 'g' L 'g' D 'u' L 'c' L 'c' # R159 (1 3 5 7 9)
  | 'g' L 'g' L 'c' D 'u' L 'c' L 'g' # R160 (1 3 5 7 9)
  | 'g' L 'g' L 'g' D 'u' L 'c' L 'u' # R161 (1 3 5 7 9)
  | 'g' L 'g' L 'u' D 'u' L 'c' L 'g' # R162 (1 3 5 7 9)
  | 'g' L 'c' L 'a' D 'u' L 'g' L 'u' # R163 (1 3 5 7 9)
  | 'g' L 'c' L 'u' D 'u' L 'g' L 'a' # R164 (1 3 5 7 9)
  | 'g' L 'c' L 'g' D 'u' L 'g' L 'c' # R165 (1 3 5 7 9)
  | 'g' L 'c' L 'c' D 'u' L 'g' L 'g' # R166 (1 3 5 7 9)
  | 'g' L 'c' L 'g' D 'u' L 'g' L 'u' # R167 (1 3 5 7 9)
  | 'g' L 'c' L 'u' D 'u' L 'g' L 'g' # R168 (1 3 5 7 9)
  | 'g' L 'g' L 'a' D 'u' L 'u' L 'u' # R169 (1 3 5 7 9)
  | 'g' L 'g' L 'u' D 'u' L 'u' L 'a' # R170 (1 3 5 7 9) 
  | 'g' L 'g' L 'g' D 'u' L 'u' L 'c' # R171 (1 3 5 7 9)
  | 'g' L 'g' L 'c' D 'u' L 'u' L 'g' # R172 (1 3 5 7 9)
  | 'g' L 'g' L 'g' D 'u' L 'u' L 'u' # R173 (1 3 5 7 9)
  | 'g' L 'g' L 'u' D 'u' L 'u' L 'g' # R174 (1 3 5 7 9)
  | 'g' L 'u' L 'a' D 'u' L 'g' L 'u' # R175 (1 3 5 7 9)
  | 'g' L 'u' L 'u' D 'u' L 'g' L 'a' # R176 (1 3 5 7 9)  
  | 'g' L 'u' L 'g' D 'u' L 'g' L 'c' # R177 (1 3 5 7 9)
  | 'g' L 'u' L 'c' D 'u' L 'g' L 'g' # R178 (1 3 5 7 9)
  | 'g' L 'u' L 'g' D 'u' L 'g' L 'u' # R179 (1 3 5 7 9)
  | 'g' L 'u' L 'u' D 'u' L 'g' L 'g' # R180 (1 3 5 7 9)
  | 'u' L 'a' L 'a' D 'g' L 'u' L 'u' # R181 (1 3 5 7 9)
  | 'u' L 'a' L 'u' D 'g' L 'u' L 'a' # R182 (1 3 5 7 9)
  | 'u' L 'a' L 'g' D 'g' L 'u' L 'c' # R183 (1 3 5 7 9)
  | 'u' L 'a' L 'c' D 'g' L 'u' L 'g' # R184 (1 3 5 7 9)
  | 'u' L 'a' L 'g' D 'g' L 'u' L 'u' # R185 (1 3 5 7 9)
  | 'u' L 'a' L 'u' D 'g' L 'u' L 'g' # R186 (1 3 5 7 9)
  | 'u' L 'u' L 'a' D 'g' L 'a' L 'u' # R187 (1 3 5 7 9)
  | 'u' L 'u' L 'u' D 'g' L 'a' L 'a' # R188 (1 3 5 7 9)
  | 'u' L 'u' L 'g' D 'g' L 'a' L 'c' # R189 (1 3 5 7 9)
  | 'u' L 'u' L 'c' D 'g' L 'a' L 'g' # R190 (1 3 5 7 9)
  | 'u' L 'u' L 'g' D 'g' L 'a' L 'u' # R191 (1 3 5 7 9)
  | 'u' L 'u' L 'u' D 'g' L 'a' L 'g' # R192 (1 3 5 7 9)
  | 'u' L 'g' L 'a' D 'g' L 'c' L 'u' # R193 (1 3 5 7 9)
  | 'u' L 'g' L 'u' D 'g' L 'c' L 'a' # R194 (1 3 5 7 9)
  | 'u' L 'g' L 'g' D 'g' L 'c' L 'c' # R195 (1 3 5 7 9)
  | 'u' L 'g' L 'c' D 'g' L 'c' L 'g' # R196 (1 3 5 7 9)
  | 'u' L 'g' L 'g' D 'g' L 'c' L 'u' # R197 (1 3 5 7 9)
  | 'u' L 'g' L 'u' D 'g' L 'c' L 'g' # R198 (1 3 5 7 9)
  | 'u' L 'c' L 'a' D 'g' L 'g' L 'u' # R199 (1 3 5 7 9)  
  | 'u' L 'c' L 'u' D 'g' L 'g' L 'a' # R200 (1 3 5 7 9)
  | 'u' L 'c' L 'g' D 'g' L 'g' L 'c' # R201 (1 3 5 7 9)
  | 'u' L 'c' L 'c' D 'g' L 'g' L 'g' # R202 (1 3 5 7 9)
  | 'u' L 'c' L 'g' D 'g' L 'g' L 'u' # R203 (1 3 5 7 9)
  | 'u' L 'c' L 'u' D 'g' L 'g' L 'g' # R204 (1 3 5 7 9)
  | 'u' L 'g' L 'a' D 'g' L 'u' L 'u' # R205 (1 3 5 7 9)
  | 'u' L 'g' L 'u' D 'g' L 'u' L 'a' # R206 (1 3 5 7 9)
  | 'u' L 'g' L 'g' D 'g' L 'u' L 'c' # R207 (1 3 5 7 9)
  | 'u' L 'g' L 'c' D 'g' L 'u' L 'g' # R208 (1 3 5 7 9)
  | 'u' L 'g' L 'g' D 'g' L 'u' L 'u' # R209 (1 3 5 7 9)
  | 'u' L 'g' L 'u' D 'g' L 'u' L 'g' # R210 (1 3 5 7 9)
  | 'u' L 'u' L 'a' D 'g' L 'g' L 'u' # R211 (1 3 5 7 9)
  | 'u' L 'u' L 'u' D 'g' L 'g' L 'a' # R212 (1 3 5 7 9)
  | 'u' L 'u' L 'g' D 'g' L 'g' L 'c' # R213 (1 3 5 7 9)
  | 'u' L 'u' L 'c' D 'g' L 'g' L 'g' # R214 (1 3 5 7 9)
  | 'u' L 'u' L 'g' D 'g' L 'g' L 'u' # R215 (1 3 5 7 9)
  | 'u' L 'u' L 'u' D 'g' L 'g' L 'g' # R216 (1 3 5 7 9)  
{% endif %}
;

L : 'a' L # L1 (1)
  | 'u' L # L2 (1)
  | 'c' L # L3 (1)
  | 'g' L # L4 (1)
  | 'a'   # 0
  | 'u'   # 0
  | 'c'   # 0
  | 'g'   # 0
  ;

 D:{% for x in range(max_dd_size) %}D{{ x }} {% endfor %} # M1 ({% for x in range(max_dd_size) %}{{ x }} {% endfor %})

E : 'a' # 0
  | 'u' # 0
  | 'c' # 0
  | 'g' # 0
  | ;

{% for x in range(max_dd_size) %}
D{{ x }} : E # N{{ x }} (0)
{% endfor %}
"""

def generate_grammar(allow_ug: bool, max_dd_size: int) -> str:
    """
    generate grammar for pseudoknot detection, based on parameters.
    """
    return (
        jinja2.Environment()
        .from_string(TEMPLATE)
        .render(
            allow_ug=allow_ug,
            max_dd_size=max_dd_size,
        )
    )
