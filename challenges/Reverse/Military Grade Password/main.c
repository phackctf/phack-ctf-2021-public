/*
   =============================================================================
   Created By : @boinc
   Created Date: Mar. 2021
   Description : Reverse challenge
   =============================================================================
*/

#include <stdlib.h>
#include <stdio.h>

int c1(char *p) {
	return p[14] * p[6] * (p[13] ^ (p[12] - p[10])) == 16335;
}

int c2(char *p) {
	return ((p[15] - p[7]) ^ p[1] ^ p[18]) == 83;
}

int c3(char *p) {
	return (p[17] - p[16]) * ((p[5] + p[9]) ^ p[0]) == -5902;
}

int c4(char *p) {
	return p[3] - p[11] == 11;
}

int c5(char *p) {
	return ((p[4] + p[2]) ^ p[8]) == 3;
}

int c6(char *p) {
	return p[15] - p[4] + p[8] == 176;
}

int c7(char *p) {
	return (((p[9] ^ p[10]) - p[18] - p[11]) ^ p[6]) == -199;
}

int c8(char *p) {
	return p[16] * p[2] + (p[0] ^ p[17]) * p[1] == 9985;
}

int c9(char *p) {
	return p[13] * p[14] - p[7] == 2083;
}

int c10(char *p) {
	return p[3] + p[12] - p[5] == 110;
}

int c11(char *p) {
	return p[13] + p[9] + p[10] * p[8] == 5630;
}

int c12(char *p) {
	return p[5] - p[16] - p[0] - p[2] == -182;
}

int c13(char *p) {
	return (p[14] ^ p[7]) * p[17] == 7200;
}

int c14(char *p) {
	return p[11] * p[6] + p[3] * p[1] == 17872;
}

int c15(char *p) {
	return p[12] - p[15] - p[4] * p[18] == -5408;
}

int c16(char *p) {
	return p[15] * p[3] + p[2] * p[11] == 18888;
}

int c17(char *p) {
	return (p[13] + p[5]) * p[16] == 15049;
}

int c18(char *p) {
	return (p[10] + p[0]) * p[17] == 12150;
}

int c19(char *p) {
	return (p[14] ^ p[6]) * p[18] == 10080;
}

int c20(char *p) {
	return p[12] + p[7] - p[4] == 132;
}

int c21(char *p) {
	return p[9] * p[1] + p[8] == 2453;
}

int check_password(char *p) {
		return c1(p) && c2(p) && c3(p) && c4(p) && c5(p) && c6(p) && c7(p) && c8(p) && c9(p) && c10(p) && c11(p) && c12(p) && c13(p) && c14(p) && c15(p) && c16(p) && c17(p) && c18(p) && c19(p) && c20(p) && c21(p);
}

int main(void) {
	char password[100];
	printf("55th Infantry Division identify checker\n");
	printf("Personal access ID: ");
	scanf("%s", password);

	if (check_password(password)) {
		printf("[+] ACCESS GRANTED!\n");
	} else {
		printf("[+] ACCES REJECTED!\n");
	}
}
