

module Q2aFSM2
(
  input clk,
  input resetn,
  input [3:1] r,
  output [3:1] g
);

  parameter A = 2'd0;parameter B = 2'd1;parameter C = 2'd2;parameter D = 2'd3;
  reg [1:0] state;reg [1:0] next_state;

  always @(posedge clk) begin
    if(!resetn) state <= A; 
    else state <= next_state;
  end


  always @(*) begin
    case(state)
      A: next_state <= (~r[1] & ~r[2] & ~r[3])? A : 
                    (~r[1] & ~r[2] & r[3])? D : 
                    (~r[1] & r[2])? C : 
                    (r[1])? B : A;
      B: next_state <= (~r[1])? A : 
                    (r[1])? B : B;
      C: next_state <= (~r[2])? A : 
                    (r[2])? C : C;
      D: next_state <= (~r[3])? A : 
                    (r[3])? D : D;
    endcase
  end

  assign g[1] = state == B;
  assign g[2] = state == C;
  assign g[3] = state == D;

endmodule

