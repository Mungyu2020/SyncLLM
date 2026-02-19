

module SimpleFSM3synchronousReset
(
  input clk,
  input in,
  input reset,
  output out
);

  reg [1:0] state;reg [1:0] next_state;
  parameter A = 2'd0;parameter B = 2'd1;parameter C = 2'd2;parameter D = 2'd3;

  always @(*) begin
    case(state)
      A: next_state <= (in)? B : A;
      B: next_state <= (in)? B : C;
      C: next_state <= (in)? D : A;
      D: next_state <= (in)? B : C;
    endcase
  end


  always @(posedge clk) begin
    if(reset) state <= A; 
    else state <= next_state;
  end

  assign out = (state == D)? 1'b1 : 1'b0;

endmodule

