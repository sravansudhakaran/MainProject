from fastai.vision import *

bs=128

ds_tfms = get_transforms(do_flip=False, flip_vert=False, max_rotate= 15,max_zoom=1.1, max_lighting=0.2, max_warp=0.2)

data = (ImageItemList.from_folder(path, convert_mode='L')
        .split_by_folder(train='training', valid='testing')
        .label_from_folder()
        .transform(tfms=ds_tfms, size=28)
        .databunch(bs=bs))
        
print(data.classes) ## Prints class labels
print(data.c) ## Prints number of classes
data.show_batch(rows=3, figsize=(10,6), hide_axis=False) ## Show sample data

class Mnist_NN(nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = nn.Linear(784, 512, bias=True) 
        self.lin2 = nn.Linear(512, 256, bias=True)
        self.lin3 = nn.Linear(256, 10, bias=True)

    def forward(self, xb):
        x = xb.view(-1,784) 
        x = F.relu(self.lin1(x))
        x = F.relu(self.lin2(x))
        return self.lin3(x)
        
mlp_learner.lr_find()
mlp_learner.recorder.plot()

mlp_learner.fit_one_cycle(5,1e-2)
