

module PS2PacketParserWithDataPath
(
  input clk,
  input [7:0] in,
  input reset,
  output [23:0] out_bytes,
  output done
);

  parameter Byte1 = 2'd0;parameter Byte2 = 2'd1;parameter Byte3 = 2'd2;parameter Done = 2'd3;
  reg [1:0] state;reg [1:0] next_state;

  always @(*) begin
    case(state)
      2'd0: next_state <= (in[3] == 1'b1)? Byte2 : Byte1;
      2'd1: next_state <= Byte3;
      2'd2: next_state <= Done;
      2'd3: next_state <= (in[3] == 1'b1)? Byte2 : Byte1;
      default: next_state <= Byte1;
    endcase
  end


  always @(posedge clk) begin
    if(reset) state <= Byte1; 
    else state <= next_state;
  end

  assign done = (state == Done)? 1'b1 : 1'b0;

  always @(posedge clk) begin
    case(state)
      2'd0: out_bytes[23:16] <= in;
      2'd1: out_bytes[15:8] <= in;
      2'd2: out_bytes[7:0] <= in;
      2'd3: out_bytes[23:16] <= in;
      default: out_bytes[23:16] <= in;
    endcase
  end


endmodule

