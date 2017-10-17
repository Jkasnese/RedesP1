//-----------------------------------------------------
// This is my second Verilog Design
// Design Name : first_counter
// File Name : first_counter.v
// Function : This is a 4 bit up-counter with
// Synchronous active high reset and
// with active high enable signal
//-----------------------------------------------------
module firstCounter (
clock , // Clock input of the design
contador,
counter_out // 4 bit vector output of the counter
); // End of port list
//-------------Input Ports-----------------------------
input clock ;

//-------------Output Ports----------------------------
output [3:0] counter_out ;
output [24:0] contador;

//-------------Input ports Data Type-------------------
// By rule all the input ports should be wires   
wire clock ;

//-------------Output Ports Data Type------------------
// Output port can be a storage element (reg) or a wire
reg [3:0] counter_out ;
reg [24:0] contador;

//------------Code Starts Here-------------------------
// Since this counter is a positive edge trigged one,
// We trigger the below block with respect to positive
// edge of the clock.
always @ (posedge clock)

// Ta correto fazer assim?
// #50000000 clk = ~clk

begin : DIVCLK // Block Name

  if (24'd0 == contador) begin
    contador <= contador+1;
	 counter_out <= counter_out+1;
  end else begin
    contador <= contador+1;
  end
end

endmodule


