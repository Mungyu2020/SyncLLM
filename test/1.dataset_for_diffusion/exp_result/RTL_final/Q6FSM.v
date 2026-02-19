

module Q6FSM
(
  input clk,
  input reset,
  input w,
  output z
);

  parameter A = 3'd0;parameter B = 3'd1;parameter C = 3'd2;parameter D = 3'd3;parameter E = 3'd4;parameter F = 3'd5;
  reg [2:0] state;reg [2:0] next_state;

  always @(posedge clk) begin
    if(reset) state <= A; 
    else state <= next_state;
  end


  always @(*) begin
    case(state)
      A: next_state <= (w)? A : B;
      B: next_state <= (w)? D : C;
      C: next_state <= (w)? D : E;
      D: next_state <= (w)? A : F;
      E: next_state <= (w)? D : E;
      F: next_state <= (w)? D : C;
      default: next_state <= A;
    endcase
  end

  assign z = (state == E) || (state == F);

endmodule

