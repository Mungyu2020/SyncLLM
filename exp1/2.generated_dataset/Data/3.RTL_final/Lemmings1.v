

module Lemmings1
(
  input clk,
  input areset,
  input bump_left,
  input bump_right,
  output walk_left,
  output walk_right
);

  parameter LEFT = 1'b0;parameter RIGHT = 1'b1;
  reg state;reg next_state;

  always @(*) begin
    case(state)
      1'b0: next_state <= (bump_left)? RIGHT : LEFT;
      1'b1: next_state <= (bump_right)? LEFT : RIGHT;
      default: next_state <= (bump_left)? RIGHT : LEFT;
    endcase
  end


  always @(posedge clk or posedge areset) begin
    if(areset) state <= LEFT; 
    else state <= next_state;
  end

  assign walk_left = (state == LEFT)? 1'b1 : 1'b0;
  assign walk_right = (state == RIGHT)? 1'b1 : 1'b0;

endmodule

