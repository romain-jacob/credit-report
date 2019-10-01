import os
import csv
import pandas as pd
import numpy as np

def parse_contrib(data_file): 
    """
    
    """

    # Load in DataFrame
    contrib = pd.read_csv(data_file, skiprows=[1,2])

    # Output table to include in tex file
    out_file = '../files/contrib.txt'
    with open(out_file, 'w', newline='') as csvfile:
        result_writer = csv.writer(csvfile,
                                   delimiter=' ',
                                   quotechar=' ',
                                   quoting=csv.QUOTE_MINIMAL)
        # Open the table
        result_writer.writerow(['\\noindent'])
        result_writer.writerow(['\\begin{longtable}[l]{',
                                '@{}',
                                'p{\colauthlen}',
                                '@{\qquad}',
                                'p{\colcontriblen}',
                                '@{\qquad}',
                                'l',
                                '@{}',
                                '}'])

        # Write header row
        result_writer.writerow(['',
                                '',
                                '\\textbf{Author}',
                                '&',
                                '\\textbf{Contributions}',
                                '&',
                                '\\textbf{Degree}',
                                '',
                                '\\\\[\minorskip]'])

        # Loop through the authors
        for i in range(len(contrib)):

            # Select the contributions on one author
            contrib_single = contrib[i:i+1].dropna(axis=1)

            # Get name, OrcID, and roles 
            name = contrib_single['Contributor'].values[0]
            if 'ORCID' in contrib_single:
                orcid = contrib_single['ORCID'].values[0]
            else: 
                orcid = ''
                print('%s: no ORCID...' %name)
            roles = contrib_single.columns[2:].values
            if len(roles) == 0:
                print('%s: no contributions...' %name)

            # Role counter
            cnt = 0

            # Single role case handling
            if len(roles) == 1:
                roles = np.append(roles, ' ')

            # Loop through the different roles
            for role in roles:

                # String to print in first column
                if cnt == 0:
                    header = name
                elif cnt == 1:
                    header = '\href{https://orcid.org/%s}{%s}' % (orcid, orcid)
                else:
                    header = ''

                # String to print in third column
                if role != ' ':
                    level = contrib_single[role].values[0]
                else:
                    level = ' '

                # Add vertical space at the end of the group
                if role == roles[-1]:
                    end_line = '\\\\[\minorskip]'
                else:
                    end_line = '\\\\'

                line = ('%s & %s & %s %s' %
                        (header,
                         role,
                         level,
                         end_line))
                result_writer.writerow([line])

                # Move to next role
                cnt += 1 

        # Close the table
        result_writer.writerow(['\\end{longtable}'])
    print('parse_contrib : Done.\n')
    
    return 

def parse_meta(meta): 
    """
    """
    
    # Output table to include in tex file
    out_file = '../files/meta.txt'
    with open(out_file, 'w', newline='') as csvfile:
        result_writer = csv.writer(csvfile,
                                   delimiter=' ',
                                   quotechar=' ',
                                   quoting=csv.QUOTE_MINIMAL)
        # Open the table
        result_writer.writerow(['\\noindent'])
        result_writer.writerow(['\\begin{tabularx}{\linewidth}{',
                                '@{}',
                                'p{\colauthlen}',
                                '@{\qquad}',
                                'X',
                                '@{}',
                                '}'])

        # Title
        result_writer.writerow(['\\textbf{Title} &',
                               meta["title"],
                               '\\\\[0.5\minorskip]'])
        # URL
        if 'url' in meta:
            if '//' in meta["url"]:
                root, address = meta["url"].split('//')
                url = '\href{https://%s}{%s}' % (address,address)
            else: 
                url = meta["url"]
            
            result_writer.writerow(['\\textbf{URL} &',
                                   url])
                
        # DOI
        if 'doi' in meta:
            doi = '\href{https://doi.dx/%s}{%s}' % (meta["doi"], meta["doi"])
            result_writer.writerow(['\\textbf{URL} &',
                                    url])

        # Close the table
        result_writer.writerow(['\\end{tabularx}'])
        
    print('parse_meta : Done.\n')    
    return 

def compile_pdf():
    os.system('pdflatex -synctex=1 -interaction=nonstopmode ../src/credit/CRediT.tex');
    os.system('mv CRediT.pdf ../files/CRediT.pdf');
    os.system('rm -f CRediT.*');
    print('compile_pdf : Done. \n')    
    return
    