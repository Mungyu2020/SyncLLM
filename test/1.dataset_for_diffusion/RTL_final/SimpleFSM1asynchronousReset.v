

module SimpleFSM1asynchronousReset
(
  input clk,
  input areset,
  input in,
  output out
);

  parameter A = 1'b0;parameter B = 1'b1;
  reg state;reg next_state;

  always @(*) begin
    case(state)
      A: next_state = (in)? A : B;
      B: next_state = (in)? B : A;
    endcase
  end


  always @(posedge clk or posedge areset) begin
    if(areset) state <= B; 
    else state <= next_state;
  end

  assign out = (state == B)? 1'b1 : 1'b0;

endmodule

