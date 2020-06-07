package hw7;

/**
 * The Fraction Class
A fraction is a number of the form numerator/denominator
 where the numerator and denominator are integers. The denominator cannot be 0. 
 You may assume that no user will input a denominator of 0.
 * @author yangzhengjie
 *
 */

public class Fraction {
	
	//Create instance variables
	/**
	 * Integers for numerator and denominator
	 */
	int numerator;
	int denominator;
	
	
	//constructor
	/**
	 * to create a Fraction with the given numerator and denominator.
	 * @param numerator
	 * @param denominator
	 */
	public Fraction(int numerator, int denominator) {
		//The constructor should set the numerator and denominator instance variables
		//in the Fraction class.
		this.numerator = numerator;
		this.denominator = denominator;
		
		//The convention is that negative fractions have the negative in the numerator.
		if(this.denominator<0) {
			this.numerator = -this.numerator;
			this.denominator = -this.denominator;
		}
		
	}
	

	/**
	 * Reduce the current fraction by eliminating common factors.
	 * Remember, the convention is that negative fractions have the negative in the
numerator.
	 */
	public void reduceToLowestForm() {
		//use gcm method to find common factors.
		int gcm = Math.abs(gcm(this.numerator, this.denominator));
		    //after the common factor 
			this.numerator =this.numerator/gcm;
			this.denominator= this.denominator/gcm;
	}
	
	
	/**
	 * find common factor gcm
	 * @param a numerator
	 * @param b denominator
	 * @return
	 */
	public static int gcm(int a, int b) {
		// use this function to conduct the common factor calculation
		return b == 0 ? a : gcm(b, a % b);
	}
	
	
	
	/**
	 * Add the current fraction to the given otherFraction.
	 * @param otherFraction
	 * @return the add result Returns a new Fraction that is the sum of the two Fractions.
	 */
	public Fraction add(Fraction otherFraction) {
		//new 
		Fraction theNewFraction= new Fraction(numerator, denominator);
		//numerator calculation
		theNewFraction.numerator = this.numerator*otherFraction.denominator+
				this.denominator*otherFraction.numerator;
		//denominator calculation
		theNewFraction.denominator = this.denominator*otherFraction.denominator;
		//The returned Fraction must be in reduced/lowest form.
		theNewFraction.reduceToLowestForm();
		//Returns a new Fraction that is the sum of the two Fractions.
		return theNewFraction;
	}
	
	
	/**
	 * Subtract the given otherFraction from the current fraction.
	 * That is, thisFraction - otherFraction.
	 * @param otherFraction
	 * @return Returns a new Fraction that is the difference of the two Fractions.
	 */
	public Fraction subtract(Fraction otherFraction) {
		
		//new 
		  Fraction theNewFraction= new Fraction(numerator, denominator);
		//numerator calculation
		  theNewFraction.numerator = this.numerator*otherFraction.denominator-
		  this.denominator*otherFraction.numerator;
		//denominator calculation
		  theNewFraction.denominator = this.denominator*otherFraction.denominator;
		//The returned Fraction must be in reduced/lowest form.
		  theNewFraction.reduceToLowestForm();
		//Returns a new Fraction that is the difference of the two Fractions.
		  return theNewFraction ;
	}
	
	
	/**
	 * Multiply the current fraction by the given otherFraction.
	 * @param otherFraction
	 * @return Returns a new Fraction that is the product of this fraction 
	 * and the otherFraction.
	 */
	public Fraction mul(Fraction otherFraction) {
		//new Fraction theNewFraction
		Fraction theNewFraction= new Fraction(numerator, denominator);
		//numerator calculation
		theNewFraction.numerator = this.numerator*otherFraction.numerator;
		//denominator calculation
		theNewFraction.denominator = this.denominator*otherFraction.denominator;
		//The returned Fraction must be in reduced/lowest form.
		theNewFraction.reduceToLowestForm();
		
		//Returns a new Fraction that is the product of this fraction and the otherFraction.
		return theNewFraction;
	}
	
	
	/**
	 * Divide the current fraction by the given otherFraction.
	 * That is, thisFraction / otherFraction.
	 * @param otherFraction
	 * @return Returns a new Fraction that is the quotient of this fraction and the otherFraction.
	 */
	public Fraction div(Fraction otherFraction) {
		//new Fraction theNewFraction
		Fraction theNewFraction= new Fraction(numerator, denominator);
		//numerator calculation
		theNewFraction.numerator = this.numerator*otherFraction.denominator;
		//denominator calculation
		theNewFraction.denominator = this.denominator*otherFraction.numerator;  
		//The returned Fraction must be in reduced/lowest form.
		theNewFraction.reduceToLowestForm();
		return theNewFraction;
	}
	
	
	/**
	 * Return this fraction in decimal form.
	 * @return
	 */
	public double decimal() {
		//use (double) to convert type
		double decimalNumber = (double)this.numerator/this.denominator;
		return decimalNumber;
	}
	
	/**
	 * Square the current fraction.
	 * This method modifies the current fraction and reduces it to lowest form.
	 */
	public void sqr() {
		//numerator calculation
		this.numerator = this.numerator *this.numerator;
		//denominator calculation
		this.denominator = this.denominator *this.denominator;
		//reduces it to lowest form
		this.reduceToLowestForm();	
	}
	
	
	/**
	 * Average the current fraction with the given otherFraction.
	 * The returned Fraction must be in reduced/lowest form.
	 * @param otherFraction
	 * @return Return a new Fraction that is the average of this fraction and the otherFraction.
	 */
	
	public Fraction average(Fraction otherFraction) {
		//new Fraction
		Fraction theNewFraction= new Fraction(numerator, denominator);
		//numerator calculation
		theNewFraction.numerator = this.numerator*otherFraction.denominator
				+this.denominator*otherFraction.numerator;
		//denominator calculation to find the average double
		theNewFraction.denominator = this.denominator*otherFraction.denominator*2;  
		//in reduced/lowest form
		theNewFraction.reduceToLowestForm();	
		return theNewFraction;

	}
	
	/**
	 * Static method to average all of the fractions in the given array.
	 *  don’t need to create an instance of the Fraction class in order to call a static method
	 * @param fractions
	 * @return
	 */
	public static Fraction average(Fraction[] fractions) {
		//two integers if there is nothing in fraction 
		// numerator = 0
		int newNumerator = 0;
		//denominator =1
		int newDenominator = 1;
		Fraction theNewFraction= new Fraction(newNumerator, newDenominator);
		//if fractions is not empty
		if (fractions.length>0) {
			//add every fraction in fractions 
			for(int i = 0;i < fractions.length;i ++) {
				theNewFraction = theNewFraction.add(fractions[i]);
				//renew the two
				newNumerator = theNewFraction.numerator;
				newDenominator = theNewFraction.denominator;
			}
			//to find the average 
			newDenominator *= fractions.length;
		}
		//a new fraction
		Fraction theNewFraction1= new Fraction(newNumerator, newDenominator);
		//reduce to lowest
		theNewFraction1.reduceToLowestForm();
		
		return theNewFraction1;
		
	}
	
	/**Static method to average all the integers in the given array.
	 *  don’t need to create an instance of the Fraction class in order to call a static method
	 * @param ints
	 * @return
	 * Return the average of the array as a new Fraction.
	 */
	public static Fraction average(int[] ints) {
		//two integers if there is nothing in fraction 
		//if empty
		int aveIntNumerator = 0;
		int aveIntDenominator = 1;
		int totalInts = 0;
		//if fractions is not empty
		if (ints.length > 0) {
			for (int i = 0; i < ints.length; i++) {
				totalInts += ints[i];
			}
			aveIntNumerator = totalInts;
			aveIntDenominator = ints.length;
		}
		//new Fraction aveInts
		Fraction aveInts = new Fraction(aveIntNumerator, aveIntDenominator);
		//reduce to lowest
		aveInts.reduceToLowestForm();
		return aveInts;
		
	}
	
	/**
	 * Overriden method to compare the given object (as a fraction) to the current fraction, for equality.
	 */
	@Override
	
	public boolean equals(Object object) {
		Fraction toTest = (Fraction) object;
		//Two fractions are considered equal if they have the same numerator and same denominator, after eliminating common factors.
		Fraction toTestClone = new Fraction(toTest.numerator,toTest.denominator);
		//This method does not (permanently) reduce the current fraction to lowest form.
		Fraction thisClone = new Fraction(this.numerator, this.denominator);
		//reduce
		toTestClone.reduceToLowestForm();
		thisClone.reduceToLowestForm();
		//check
		if (thisClone.numerator == toTestClone.numerator) {
			//check again
			if (thisClone.denominator == toTestClone.denominator) {
				return true;
			}
		}
		return false;

	}
	/**
	 * Overriden method to return a string representation of the current fraction.
	 */
	@Override
	public String toString() {
		//There is a no whitespace in this string.
		String fracString = (numerator +"/"+denominator);
		return fracString;
	}	
	

}
