1.Unzip CIS700.zip.

2.Download CelebA dataset from https://www.kaggle.com/jessicali9530/celeba-dataset and unzip archive.zip to CIS700 folder. Now, there is a folder named img_align_celeba in your CIS700 folder.

3.Training:	Make sure current path is 'Your path/CIS700', and run the following code in your terminal
		python train.py --dataset_path img_align_celeba --data_file CelebA_txt\train.txt --batch_size 10 --lr 2e-4 --epochs 10

4.Find the dictionary for trained model named '10_net_DMFN.pth' in 'Your path/checkpoints'. It was saved in the newest folder. Copy it to 'CIS700/pretrained'.

5.Testing: 	Make sure current path is 'Your path/CIS700' and run the following code in your terminal 
		python test.py --dataset img_align_celeba --data_file CelebA_txt\test.txt --load_model_dir pretrained

6.Check the results in 'CIS700/test_results'. Outputs(inpainted image) and inputs(with masked region) are stored in the newest folder.