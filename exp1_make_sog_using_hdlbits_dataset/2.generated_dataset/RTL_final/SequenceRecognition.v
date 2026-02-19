

module SequenceRecognition
(
  input clk,
  input reset,
  input in,
  output disc,
  output flag,
  output err
);

  parameter A = 0;parameter B = 1;parameter C = 2;parameter D = 3;parameter E = 4;parameter F = 5;parameter G = 6;parameter DISC = 7;parameter ERR = 8;parameter FLAG = 9;
  reg [3:0] state;reg [3:0] next_state;

  always @(posedge clk) begin
    if(reset) state <= A; 
    else state <= next_state;
  end


  always @(*) begin
    case(state)
      A: next_state <= (in)? B : A;
      B: next_state <= (in)? C : A;
      C: next_state <= (in)? D : A;
      D: next_state <= (in)? E : A;
      E: next_state <= (in)? F : A;
      F: next_state <= (in)? G : DISC;
      DISC: next_state <= (in)? B : A;
      G: next_state <= (in)? ERR : FLAG;
      FLAG: next_state <= (in)? B : A;
      ERR: next_state <= (in)? ERR : A;
      default: next_state <= A;
    endcase
  end

  assign disc = state == DISC;
  assign flag = state == FLAG;
  assign err = state == ERR;

endmodule

