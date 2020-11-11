macro "make_oval_ring" {
//Create a Dialog
Dialog.create("Initialization");
Dialog.addNumber("x_center:", 524);
Dialog.addNumber("y_center:", 502);
Dialog.addNumber("diameter:", 913);
Dialog.addNumber("ring_number:", 30);
Dialog.addNumber("pixel:", 0.05);
Dialog.show();

x_center = Dialog.getNumber();
y_center = Dialog.getNumber();
diameter = Dialog.getNumber();
ring_number = Dialog.getNumber();
pixel = Dialog.getNumber();
num_oval = ring_number;
radius = diameter/2;

//Create Oval
for (i = 0; i < num_oval; i++) 
{
	diameter_min = diameter-2*pixel*i;
	radius = diameter_min/2;
	makeOval(x_center-radius, y_center-radius, diameter_min, diameter_min);
	roiManager("Add");
	roiManager("Select", i);
	roiManager("Rename", i+1);
}
//Create Ring
for (j = 1; j <num_oval-1; j++) {
	roiManager("Select", newArray(j,j+1));
	roiManager("XOR");
	roiManager("Add");
	ring_number = num_oval+j-1;
	roiManager("Select",ring_number);
	roiManager("Rename", "ring"+j);	
	}
}
