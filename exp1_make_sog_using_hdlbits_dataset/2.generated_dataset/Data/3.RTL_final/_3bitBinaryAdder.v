

module _3bitBinaryAdder
(
  input [2:0] a,
  input [2:0] b,
  input cin,
  output [2:0] cout,
  output [2:0] sum
);

  wire [2:0] cout1;

  fadd
  f1
  (
    a[0],
    b[0],
    cin,
    cout1[0],
    sum[0]
  );


  fadd
  f2
  (
    a[1],
    b[1],
    cout1[0],
    cout1[1],
    sum[1]
  );


  fadd
  f3
  (
    a[2],
    b[2],
    cout1[1],
    cout1[2],
    sum[2]
  );

  assign cout = cout1;

endmodule



module fadd
(
  input a,
  input b,
  input cin,
  output cout,
  output sum
);

  assign sum = a ^ b ^ cin;
  assign cout = a & b | b & cin | a & cin;

endmodule

