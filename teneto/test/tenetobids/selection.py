import teneto 

def test_define(): 
    tnet = teneto.TenetoBIDS(teneto.__path__[0] + '/data/testdata/dummybids/',pipeline='fmriprep',raw_data_exists=False) 
    assert len(tnet.get_selected_files(quiet=1)) == 6

def test_define_sub_then_task(): 
    tnet = teneto.TenetoBIDS(teneto.__path__[0] + '/data/testdata/dummybids/',pipeline='fmriprep',subjects='001',raw_data_exists=False) 
    assert len(tnet.get_selected_files(quiet=1)) == 3    
    tnet.set_tasks('a')
    assert len(tnet.get_selected_files(quiet=1)) == 2

def test_define_run_then_sub(): 
    tnet = teneto.TenetoBIDS(teneto.__path__[0] + '/data/testdata/dummybids/',pipeline='fmriprep',runs='alpha',raw_data_exists=False) 
    assert len(tnet.get_selected_files(quiet=1)) == 4
    tnet.set_subjects('001')
    assert len(tnet.get_selected_files(quiet=1)) == 2

def test_define_task_then_run(): 
    tnet = teneto.TenetoBIDS(teneto.__path__[0] + '/data/testdata/dummybids/',pipeline='fmriprep',tasks='a',raw_data_exists=False) 
    assert len(tnet.get_selected_files(quiet=1)) == 4
    tnet.set_runs('beta')    
    assert len(tnet.get_selected_files(quiet=1)) == 2
    