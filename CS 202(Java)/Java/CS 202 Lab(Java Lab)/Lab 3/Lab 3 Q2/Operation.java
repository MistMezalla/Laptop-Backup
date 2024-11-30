public class Operation{
	private int operand1;
	private String operator;
	private int operand2;
	private double result;

	void calculateValue()
	{	
		if (operator.equals("+"))
		{
			result = operand1 + operand2;
		}
		else if (operator.equals("-"))
		{
			result = operand1 - operand2;
		}
		else if (operator.equals("*"))
		{
			result = operand1 * operand2;
		}
		else if (operator.equals("/"))
		{
			result = (double)operand1 / operand2;
		}
		else
		{
			System.out.println("Wrong operator!!!");
		}
	}
	
	void displayResult()
	{
		System.out.printf("%d %s %d = %f\n",operand1,operator,operand2,result);
	} 

	Operation(int op1,String op, int op2){
		this.operand1 = op1;
		this.operator = op;
		this.operand2 = op2;
	}	
	
}
	
	

	