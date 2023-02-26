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
	
	// Initialize n, e, C, d
	BN_hex2bn(&n, "3A01FB9D00D64A8299D89E01EB02B2D3F88992C804ECDC1058EFB475CEA4EE3");
	BN_hex2bn(&e, "34A8D");
	BN_hex2bn(&C, "ED3C75C55905421A53FDB335D0E48FE0C38DECC6F2B0E2403F217586867ED0");
	BN_hex2bn(&d, "0251F9BE6FFE4C385794BED039864BBC1B1F3324A542D9597F8AF00C7306A5F5");

	// res = c^d mod n
	BN_mod_exp(M, C, d, n, ctx);
	printBN("M = C^d mod n = ", M);
	return 0;
}
