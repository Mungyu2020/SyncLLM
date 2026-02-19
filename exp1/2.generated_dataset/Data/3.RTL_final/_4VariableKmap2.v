

module _4VariableKmap2
(
  input a,
  input b,
  input c,
  input d,
  output out
);

  assign out = a | c & ~b;

endmodule

