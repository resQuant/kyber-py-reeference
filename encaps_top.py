import kyber
import argparse
import base64

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--security", type=int, choices=[2,3,5], default=2,
                    help="Select security level")
    parser.add_argument("-v", "--verbose", action="store_true",
                    help="Print intermediate values")
    parser.add_argument("-k", "--keyfile", required=True, help="File storing private key")
    parser.add_argument("-m", "--message", required=True, help="Ciphertext file")

    args = parser.parse_args()

    sec_lvl = args.security
    file_arg = args.keyfile
    msg_file_arg = args.message
    sk_file_arg = file_arg

    f = open(sk_file_arg, mode="rb")
    pk = f.read()
    f.close()
    f = open(msg_file_arg, mode="rb")
    m = f.read()
    f.close()
    
    if sec_lvl == 2:
        ss = kyber.Kyber512.enc(pk)
    elif sec_lvl == 3:
        ss = kyber.Kyber768.enc(pk)
    else:
        ss = kyber.Kyber1024.enc(pk)


    
    print(hex(ss))
    

    if args.verbose:
        print(base64.b64encode(ss))
