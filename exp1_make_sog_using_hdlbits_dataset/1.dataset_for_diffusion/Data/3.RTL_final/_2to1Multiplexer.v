

module _2to1Multiplexer
(
  input a,
  input b,
  input sel,
  output out
);

  assign out = (sel)? b : a;

endmodule

