#include <stdio.h>
#include <openssl/bn.h>
void printBN(char *msg, BIGNUM * a) {
	char * number_str = BN_bn2hex(a);
	printf("%s %s\n", msg, number_str);
	OPENSSL_free(number_str);
}
int main () {
	BN_CTX *ctx = BN_CTX_new();
	BIGNUM *M = BN_new();
	BIGNUM *S = BN_new();
	BIGNUM *e = BN_new();
	BIGNUM *n = BN_new();
	
	// Initialize S, e, n
	BN_hex2bn(&S, "03AC5204A8B69CE6B565C818C47F6263BC1C2290F400AF199BB097BCAECCFCBF");
	BN_hex2bn(&e, "88D35");
	BN_hex2bn(&n, "605A933FFBFEAEB8E290D31D9894B9646FF967D21A9D420680F8FA390855097");

	// M = S^e mod n
	BN_mod_exp(M, S, e, n, ctx);
	printBN("M = S^e mod n = ", M);
	return 0;
}
