# calculadora.py
import argparse

parser = argparse.ArgumentParser(description="Calculadora, suma/resta/multiplica a y b")
parser.add_argument("-a", "--numero_a", type=int, help="Parametro a")
parser.add_argument("-b", "--numero_b", type=int, help="Parametro b")
parser.add_argument("-o", "--operacion",
                    type=str,
                    choices=["suma", "resta", "multiplicacion"],
                    default="suma", required=False,
                    help="Operacion a realizar con a y b")

args = parser.parse_args()

if args.operacion == "suma":
    print(args.numero_a + args.numero_b)
elif args.operacion == "resta":
    print(args.numero_a - args.numero_b)
elif args.operacion == "multiplicacion":
    print(args.numero_a * args.numero_b)