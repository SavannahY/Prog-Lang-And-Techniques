package hw7;

import static org.junit.Assert.assertEquals;
import static org.junit.jupiter.api.Assertions.*;


import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class FractionTest {
	int numerator;
	int denominator;
	
	Fraction normalFrac;
	Fraction normalFrac2;
	Fraction minusFrac;
	Fraction zeroFrac;
	Fraction addFrac1;
	Fraction addFrac2;
	Fraction addFrac3;
	Fraction addFrac4;
	Fraction zeroFrac1;

	@BeforeEach
	void setUp() throws Exception {
		this.normalFrac = new Fraction(2,3);
		this.normalFrac2 = new Fraction(2,8);
		
		this.minusFrac = new Fraction(2,-8);
		this.zeroFrac = new Fraction(0,4);
		
		this.addFrac1 = new Fraction(3,5);
		this.addFrac2 = new Fraction(1,4);
		
		this.addFrac3 = new Fraction(-1,2);
		this.addFrac4 = new Fraction(2,-3);
		
		this.zeroFrac1 = new Fraction(0,1);	
	}



	@Test
	void testReduceToLowestForm() {
		this.normalFrac.reduceToLowestForm();
		this.normalFrac2.reduceToLowestForm();
		this.minusFrac.reduceToLowestForm();
		this.zeroFrac.reduceToLowestForm();
		
		assertEquals(2,this.normalFrac.numerator);
		assertEquals(3,this.normalFrac.denominator);
		
		assertEquals(1,this.normalFrac2.numerator);
		assertEquals(4,this.normalFrac2.denominator);
		
		assertEquals(-1,this.minusFrac.numerator);
		assertEquals(4,this.minusFrac.denominator);
		
		assertEquals(0,this.zeroFrac.numerator);
		assertEquals(1,this.zeroFrac.denominator);
	}

	@Test
	void testGcm() {
		
		int firstGcm = Fraction.gcm(100 , 10);
		assertEquals(10,firstGcm);
		
		int secondGcm = Fraction.gcm(100 , -10);
		assertEquals(-10,secondGcm);
		
		int thirdGcm = Fraction.gcm(5 , 3);
		assertEquals(1,thirdGcm);
		

		
	}

	@Test
	void testAdd() {
		assertEquals(11,this.normalFrac.add(normalFrac2).numerator);
		assertEquals(12,this.normalFrac.add(normalFrac2).denominator);
		
		assertEquals(17,this.addFrac1.add(addFrac2).numerator);
		assertEquals(20,this.addFrac1.add(addFrac2).denominator);
		
		assertEquals(-7,this.addFrac3.add(addFrac4).numerator);
		assertEquals(6,this.addFrac3.add(addFrac4).denominator);
		
	}

	@Test
	void testSubtract() {
		assertEquals(5,this.normalFrac.subtract(normalFrac2).numerator);
		assertEquals(12,this.normalFrac.subtract(normalFrac2).denominator);
		
		assertEquals(7,this.addFrac1.subtract(addFrac2).numerator);
		assertEquals(20,this.addFrac1.subtract(addFrac2).denominator);
		
		//System.out.println(this.addFrac3.subtract(addFrac4).numerator);
		//System.out.println(this.addFrac3.subtract(addFrac4).denominator);	
		
		assertEquals(1,this.addFrac3.subtract(addFrac4).numerator);
		assertEquals(6,this.addFrac3.subtract(addFrac4).denominator);

	}

	@Test
	void testMul() {
		assertEquals(11,this.normalFrac.add(normalFrac2).numerator);
		assertEquals(12,this.normalFrac.add(normalFrac2).denominator);
		
		assertEquals(17,this.addFrac1.add(addFrac2).numerator);
		assertEquals(20,this.addFrac1.add(addFrac2).denominator);
		
		assertEquals(-7,this.addFrac3.add(addFrac4).numerator);
		assertEquals(6,this.addFrac3.add(addFrac4).denominator);
		
	}

	@Test
	void testDiv() {
		assertEquals(11,this.normalFrac.add(normalFrac2).numerator);
		assertEquals(12,this.normalFrac.add(normalFrac2).denominator);
		
		assertEquals(17,this.addFrac1.add(addFrac2).numerator);
		assertEquals(20,this.addFrac1.add(addFrac2).denominator);
		
		assertEquals(-7,this.addFrac3.add(addFrac4).numerator);
		assertEquals(6,this.addFrac3.add(addFrac4).denominator);

	}

	@Test
	void testDecimal() {
		assertEquals(addFrac1.decimal(),0.6,0.01);
		assertEquals(addFrac2.decimal(),0.25,0.001);
		assertEquals(addFrac4.decimal(),-0.667,0.01);
	}

	@Test
	void testSqr() {
		
		addFrac3.sqr();
		assertEquals("1/4",addFrac3.toString());
		addFrac4.sqr();
		assertEquals("4/9",addFrac4.toString());
		zeroFrac1.sqr();
		assertEquals("0/1",zeroFrac1.toString());

	}

	@Test
	void testAverageFraction() {
		this.addFrac3 = new Fraction(-1,2);
		this.addFrac4 = new Fraction(2,-3);
		assertEquals(-7,this.addFrac3.average(addFrac4).numerator);
		assertEquals(12,this.addFrac3.average(addFrac4).denominator);
		System.out.println(this.addFrac3.average(addFrac4).numerator);
		System.out.println(this.addFrac3.average(addFrac4).denominator);
	}

	@Test
	void testAverageFractionArray() {
		Fraction[] myArrayOfFractions1 = {new Fraction(3,4), new Fraction(3,5), new Fraction(3,6)};
		Fraction f1 = Fraction.average(myArrayOfFractions1);
		assertEquals("37/60", f1.toString());
		Fraction[] myArrayOfFractions2 = {};
		Fraction f2 = Fraction.average(myArrayOfFractions2);
		assertEquals("0/1", f2.toString());
		Fraction[] myArrayOfFractions3 = {new Fraction(-1,24), new Fraction(2,-24), new Fraction(5,-24)};
		Fraction f3 = Fraction.average(myArrayOfFractions3);
		assertEquals("-1/9", f3.toString());
	}

	@Test
	void testAverageIntArray() {
		int[] myArrayOfInts2 = {};
		Fraction f2 = Fraction.average(myArrayOfInts2);
		assertEquals("0/1", f2.toString());
		int[] myArrayOfInts1 = {1,2,3,4,5};
		Fraction f1 = Fraction.average(myArrayOfInts1);
		assertEquals("3/1", f1.toString());
		int[] myArrayOfInts3 = {1,2,3,4};
		Fraction f3 = Fraction.average(myArrayOfInts3);
		assertTrue(new Fraction(5,2).equals(f3));
	}

	@Test
	void testEqualsObject() {
		assertTrue(this.normalFrac.equals(new Fraction(4,6)));
		assertTrue(normalFrac2.equals(new Fraction(1,4)));
		assertTrue(this.zeroFrac1.equals(new Fraction(0,-100000)));

	}

	@Test
	void testToString() {
		assertEquals("2/3", normalFrac.toString());
		assertEquals("2/8", normalFrac2.toString());
		assertEquals("0/1", zeroFrac1.toString());
		assertEquals("-2/3", addFrac4.toString());
		

		
	}

}
