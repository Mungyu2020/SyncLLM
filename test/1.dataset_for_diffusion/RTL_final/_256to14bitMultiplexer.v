

module _256to14bitMultiplexer
(
  input [1023:0] in,
  input [7:0] sel,
  output [3:0] out
);

  assign out = in[sel*4:sel*4+4];

endmodule

