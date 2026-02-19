

module SimpleFSM1synchronousReset
(
  clk,
  reset,
  in,
  out
);

  input clk;
  input reset;
  input in;
  output out;
  reg out;
  parameter A = 1'b0;parameter B = 1'b1;
  reg present_state;reg next_state;

  always @(posedge clk) begin
    if(reset) begin
      present_state <= B;
    end else begin
      present_state = next_state;
    end
  end


  always @(*) begin
    case(present_state)
      A: begin
        next_state <= (in)? A : B;
        out <= 1'b0;
      end
      B: begin
        next_state <= (in)? B : A;
        out <= 1'b1;
      end
    endcase
  end


endmodule

