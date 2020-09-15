EMPTY_GRAPH = """
digraph EMPTY {
}
"""

FLOWCHART = """
digraph FLOWCHART {

  a  [label="node one"]
  b  [label="node two"]
  c  [label="node three"]

  a -> b -> c

}
"""

SIMPLE_CFSM = """
digraph G {

}
"""

COMPLEX_CFSM = """
digraph G {
compound = true;
"220" [ label="220: " ];
"220" -> "222" [ label="Svr!Init(Config)" ];
"227" [ label="227: " ];
"227" -> "228" [ label="Svr!Attack(Location)" ];
"228" [ label="228: " ];
"228" -> "222" [ label="Svr?Hit(Location)" ];
"228" -> "222" [ label="Svr?Miss(Location)" ];
"228" -> "222" [ label="Svr?Sunk(Location)" ];
"228" -> "221" [ label="Svr?Winner(Location)" ];
"221" [ label="221: " ];
"222" [ label="222: __Battleships_Game__P1_Svr_P2__" ];
"222" -> "223" [ label="Svr?Hit(Location)" ];
"222" -> "225" [ label="Svr?Miss(Location)" ];
"222" -> "227" [ label="Svr?Sunk(Location)" ];
"222" -> "221" [ label="Svr?Loser(Location)" ];
"223" [ label="223: " ];
"223" -> "224" [ label="Svr!Attack(Location)" ];
"224" [ label="224: " ];
"224" -> "222" [ label="Svr?Hit(Location)" ];
"224" -> "222" [ label="Svr?Miss(Location)" ];
"224" -> "222" [ label="Svr?Sunk(Location)" ];
"224" -> "221" [ label="Svr?Winner(Location)" ];
"225" [ label="225: " ];
"225" -> "226" [ label="Svr!Attack(Location)" ];
"226" [ label="226: " ];
"226" -> "222" [ label="Svr?Hit(Location)" ];
"226" -> "222" [ label="Svr?Miss(Location)" ];
"226" -> "222" [ label="Svr?Sunk(Location)" ];
"226" -> "221" [ label="Svr?Winner(Location)" ];
}
"""

PRUNED_COMPLEX_CFSM = """
digraph G {
compound=true;
"220" [label="220: "];
"223" [label="223: "];
"224" [label="224: "];
"221" [label="221: "];
"222" [label="222: __Battleships_Game__P1_Svr_P2__"];
"224" -> "221"  [label="Svr?Winner(Location)"];
"224" -> "222"  [label="Svr?Sunk(Location)"];
"222" -> "221"  [label="Svr?Loser(Location)"];
"222" -> "223"  [label="Svr?Hit(Location)"];
"222" -> "223"  [label="Svr?Miss(Location)"];
"222" -> "223"  [label="Svr?Sunk(Location)"];
"223" -> "224"  [label="Svr!Attack(Location)"];
"220" -> "222"  [label="Svr!Init(Config)"];
}
"""