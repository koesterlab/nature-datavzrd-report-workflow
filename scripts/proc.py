import pandas as pd
import os

# Define cell types and their corresponding highly-variable genes
highly_variable_genes = {
    "definitive endoterm": [
        "Afp", "Amot", "Cdx2", "Cer1", "Cldn6", "Cxcr4", "Dkk1", "Dsp", "Eomes", "Epha2", "Fgf8", "Foxa1", "Foxa2", "Gata4", "Gata6", "Hhex", "Hnf1b", "Hnf4a", "Ihh", "Irx1", "Irx3", "Klf5", "Krt19", "Lefty1", "Lhx1", "Mixl1", "Nanog", "Nodal", "Otx2", "Pcsk6", "Plet1", "Prdm1", "Smad3", "Sox17", "Tdgf1", "Tmprss2"
    ],
    "allantois": [
        "Angpt1", "Cdx1", "Cdx2", "Cdx4", "Dab2", "Dkk1", "Flt1", "Hoxa10", "Hoxa11", "Kdr", "Nodal", "Rspo3", "Slc31a1", "T", "Tbx4", "Tbx5", "Tek", "Tfap2c"
    ],
    "first heart field": [
        "Actb", "Actc1", "Bmp2", "Bmp4", "Dkk1", "Etv2", "Fgf8", "Foxc2", "Foxf1", "Gata4", "Gata5", "Gata6", "Hand1", "Hand2", "Irx2", "Irx4", "Kdr", "Mef2c", "Mesp1", "Mycn", "Myh6", "Myh7", "Myl2", "Myl4", "Myl7", "Nkx2-5", "Nodal", "Nppa", "Pdgfra", "Six1", "Smarcd3", "Smyd1", "Snai1", "Tbx20", "Tbx3", "Tbx5", "Tnnt2", "Wnt2", "Wnt8a"
    ],
    "pancreas": [
        "Bcl2", "Btbd17", "Btg2", "C2cd4c", "Cadm1", "Casz1", "Cbfa2t3", "Cck", "Cdkn1c", "Cel", "Cer1", "Ckb", "Cldn12", "Col18a1", "Cotl1", "Cpt2", "Crp", "Crybb1", "Cyb5r3", "Dab1", "Dlk1", "Dll1", "Efhd2", "Epb42", "Eya2", "Fam110a", "Fgd4", "Foxa2", "Foxa3", "Gadd45a", "Gata4", "Gcg", "Gck", "Gfra3", "Ghrl", "Gpx2", "Grin3a", "Hes6", "Hnf1a", "Hpca", "Ifitm2", "Igfbpl1", "Irs2", "Kirrel2", "Klf13", "Krt19", "Krt8", "Krtap17-1", "Lingo1", "Lmna", "Lynx1", "Mafb", "Megf11", "Mfng", "Mia", "Miat", "Mmd2", "Mnx1", "Nav2", "Ndrg1", "Neurod1", "Neurod2", "Nfix", "Nkx2-2", "Nkx6-1", "Notum", "Nptx1", "Nr5a2", "Obscn", "Onecut1", "Pde1c", "Pla2g2f", "Plk3", "Prss8", "Qsox1", "Rab15", "Rap1gap2", "Rasgrp3", "Rbfox3", "Rhbg", "Rph3al", "Rsad2", "Serinc2", "Serpina1c", "Sftpc", "Sh3bgrl3", "Shf", "Smoc2", "Sparc", "Spint2", "Spp1", "Spsb4", "Sst", "St3gal6", "St6galnac2", "Steap1", "Stxbp1", "Tbc1d8", "Tff3", "Tgm2", "Tinagl1", "Tle6", "Tmed4", "Tmem176b", "Tox3", "Tpm1"
    ]
}

# Function to process a single CSV file
def process_csv(file_path, cell_type):
    # Read the file
    df = pd.read_csv(file_path, header=None, names=["Genes", "PMID"], delimiter=';')

    # Split genes column by "," and trim whitespace
    df = df.assign(Genes=df["Genes"].str.split(",")).explode("Genes")
    df["Genes"] = df["Genes"].str.strip()

    # Add cell type column
    df["Cell Type"] = cell_type

    # Add highly-variable column
    highly_variable_set = set(highly_variable_genes[cell_type])
    df["Highly-Variable"] = df["Genes"].apply(lambda gene: "Yes" if gene in highly_variable_set else "No")

    return df

# Main function to process all files
def main():
    # Define the input files with absolute paths
    input_files = {
        "/Users/felixwiegand/Desktop/pancreas.csv": "pancreas",
        "/Users/felixwiegand/Desktop/first heart field.csv": "first heart field",
        "/Users/felixwiegand/Desktop/allantois.csv": "allantois",
        "/Users/felixwiegand/Desktop/definitive endoterm.csv": "definitive endoterm"
    }

    # Initialize an empty DataFrame for the final result
    final_df = pd.DataFrame()

    # Process each file
    for file_path, cell_type in input_files.items():
        if os.path.exists(file_path):
            processed_df = process_csv(file_path, cell_type)
            final_df = pd.concat([final_df, processed_df], ignore_index=True)
        else:
            print(f"File {file_path} not found.")

    # Save the final result to a new CSV file
    final_df.to_csv("processed_genes.csv", index=False, sep=";")
    print("Processing complete. Output saved to 'processed_genes.csv'.")

if __name__ == "__main__":
    main()
