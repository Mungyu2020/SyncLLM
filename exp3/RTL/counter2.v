module counter2 (
    input wire clk,       
    input wire rst,       
    input wire en,        
    output reg [2:0] out 
);

always @(posedge clk or negedge rst) begin
    if (!rst) begin
        out <= 8'b0;      
    end else if (en) begin
        out <= out + 1;   
    end
end

endmodule