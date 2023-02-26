#include <stdio.h>
#include <openssl/bn.h>
void printBN(char *msg, BIGNUM * a) {
	char * number_str = BN_bn2hex(a);
	printf("%s %s\n", msg, number_str);
	OPENSSL_free(number_str);
}
int main () {
	BN_CTX *ctx = BN_CTX_new();
	BIGNUM *S = BN_new();
	BIGNUM *M = BN_new();
	BIGNUM *d = BN_new();
	BIGNUM *n = BN_new();
	
	// Initialize S, M, d, n
	BN_hex2bn(&n, "3A01FB9D00D64A8299D89E01EB02B2D3F88992C804ECDC1058EFB475CEA4EE3");
	BN_hex2bn(&M, "506c6174653a205959585220343831202d3e20496c6c6567616c205475726e");
	BN_hex2bn(&d, "0251F9BE6FFE4C385794BED039864BBC1B1F3324A542D9597F8AF00C7306A5F5");

	// S = M^d mod n
	BN_mod_exp(S, M, d, n, ctx);
	printBN("S = M^d mod n = ", S);
	return 0;
}
