

module _256to1Multiplexer
(
  input [255:0] in,
  input [7:0] sel,
  output out
);

  assign out = in[sel];

endmodule

