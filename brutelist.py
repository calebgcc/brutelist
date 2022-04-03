#
#                         TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT                
#                         TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT                 
#                                               TTTT                                  
#   BBBBBBBBB       RRRRRRRRRR    UU       UU   TTTT    EEEEEEEEEE       
#   BB      B       RR       R    UU       UU   TTTT   EEEE                
#   BB      B       RR       R    UU       UU   TTTT   EEE                
#   BB      B       RRRRRRRRRR    UU       UU   TTTT   EEEEEEEEE         
#   BBBBBBBBBBBBB   RR   R R      UU       UU   TTTT   EEEEEEEEE         
#   BB          B   RR    R R     UU       UU   TTTT   EEE                
#   BB          B   RR     R R    UU       UU   TTTT   EEEE                
#   BBBBBBBBBBBBB   RR      R R   UUUUUUUUUUU   TTTT    EEEEEEEEEE         
# 

import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)

    parser.add_argument('-t','--template',dest='template',default='template',help='Template file path')
    parser.add_argument('-o','--output',dest='output',default='password_list', help='Output file path')
    group.add_argument('-s','--seed',dest='seed', help='Seed file path')
    group.add_argument('-l','--list',dest='list', type=str,nargs='+', help='List of seeds')
    
    args = parser.parse_args()

    seed_list = []
    if args.seed is not None:
        with open(args.seed,'r') as seed_file:
            seed_list = [line.strip('\n\t') for line in seed_file]
    else:
        seed_list = args.list

    with open(args.template,'r') as template_file:
        with open(args.output,'w') as output_file:
            for line in template_file:
                for seed in seed_list:
                    output_file.write(line.format(seed))





if __name__ == '__main__':
    main()