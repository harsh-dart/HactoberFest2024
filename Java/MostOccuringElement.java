package com.company.milestone;

import java.util.Scanner;

public class Demo6 {
public static void main(String[]args) {
			Scanner scanner = new Scanner(System.in);
			int [] array = new int[10];
			for (int i=0;i<array.length;i++) {
				System.out.println("Enter number "+i);
				array[i]=scanner.nextInt();
			}
			int mostoccur=array[0];
			int maxcount =0;
			for(int i=0;i<array.length;i++) {
				int count=0;
				for(int j=0;j<array.length;j++) {
					if(array[j]==array[i]) {
						count++;
					}
				}
				if(count>maxcount) {
					maxcount=count;
					mostoccur=array[i];
				}
			}
			System.out.println("Most occured element is "+mostoccur+" and "+maxcount+" times it repeated.");
			scanner.close();
		}

	}
