

module SimpleFSM2asycnhronousReset
(
  input clk,
  input areset,
  input j,
  input k,
  output out
);

  parameter OFF = 0;parameter ON = 1;
  reg state;reg next_state;

  always @(*) begin
    case(state)
      ON: next_state <= (k)? OFF : ON;
      OFF: next_state <= (j)? ON : OFF;
    endcase
  end


  always @(posedge clk or posedge areset) begin
    if(areset) state <= OFF; 
    else state <= next_state;
  end

  assign out = (state == ON)? 1'b1 : 1'b0;

endmodule

