#include <stdio.h>
#include <openssl/bn.h>
void printBN(char *msg, BIGNUM * a) {
	char * number_str = BN_bn2hex(a);
	printf("%s %s\n", msg, number_str);
	OPENSSL_free(number_str);
}
int main () {
	BN_CTX *ctx = BN_CTX_new();
	BIGNUM *n = BN_new();
	BIGNUM *e = BN_new();
	BIGNUM *M = BN_new();
	BIGNUM *d = BN_new();
	BIGNUM *C = BN_new();
	BIGNUM *res = BN_new();
	
	// Initialize n, e, M, d
	BN_hex2bn(&n, "3A01FB9D00D64A8299D89E01EB02B2D3F88992C804ECDC1058EFB475CEA4EE3");
	BN_hex2bn(&e, "34A8D");
	BN_hex2bn(&M, "506c6174653a204c53524520383435202d3e204661696c65642053746f70");
	BN_hex2bn(&d, "0251F9BE6FFE4C385794BED039864BBC1B1F3324A542D9597F8AF00C7306A5F5");

	// C = M^e mod n
	BN_mod_exp(C, M, e, n, ctx);
	printBN("C = M^e mod n = ", C);
	
	printBN("Orignial M is ", M);
	//verifying if it was encrypted properly
	// res = c^d mod n
	BN_mod_exp(res, C, d, n, ctx);
	printBN("res = C^d mod n = ", res);
	printf("res should matchs orginial M\n");
	return 0;
}
