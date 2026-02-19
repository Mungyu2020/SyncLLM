

module Lemmings2
(
  input clk,
  input areset,
  input bump_left,
  input bump_right,
  input ground,
  output walk_left,
  output walk_right,
  output aaah
);

  parameter LEFT = 2'd0;parameter RIGHT = 2'd1;parameter GROUND = 2'd2;
  reg [1:0] state;reg [1:0] next_state;reg [1:0] prev_state;

  always @(*) begin
    case(state)
      2'd0: begin
        next_state <= (!ground)? GROUND : 
                      (bump_left)? RIGHT : LEFT;
        prev_state <= LEFT;
      end
      2'd1: begin
        next_state <= (!ground)? GROUND : 
                      (bump_right)? LEFT : RIGHT;
        prev_state <= RIGHT;
      end
      2'd2: next_state <= (!ground)? GROUND : prev_state;
      default: begin
        next_state <= (!ground)? GROUND : 
                      (bump_left)? RIGHT : LEFT;
        prev_state <= LEFT;
      end
    endcase
  end


  always @(posedge clk or posedge areset) begin
    if(areset) state <= LEFT; 
    else state <= next_state;
  end

  assign walk_left = (state == LEFT)? 1'b1 : 1'b0;
  assign walk_right = (state == RIGHT)? 1'b1 : 1'b0;
  assign aaah = (state == GROUND)? 1'b1 : 1'b0;

endmodule

