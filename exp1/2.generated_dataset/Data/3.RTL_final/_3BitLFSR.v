

module _3BitLFSR
(
  input [2:0] SW,
  input [1:0] KEY,
  output [2:0] LEDR
);


  always @(posedge KEY[0]) begin
    LEDR[0] <= (KEY[1])? SW[0] : LEDR[2];
    LEDR[1] <= (KEY[1])? SW[1] : LEDR[0];
    LEDR[2] <= (KEY[1])? SW[2] : LEDR[2] ^ LEDR[1];
  end


endmodule

