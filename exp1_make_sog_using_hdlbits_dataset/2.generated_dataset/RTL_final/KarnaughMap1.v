

module KarnaughMap1
(
  input [4:1] x,
  output f
);

  assign f = ~x[1] & x[3] | x[4] & x[2];

endmodule

