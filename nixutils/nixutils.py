import sys
import subprocess
import hashlib

__author__ = 'Kevin K. <kbknapp@gmail.com>'

__VERSION = '1.0'
__VALID_ARGS = {'-v':'Display version','--version': ''}

def shred_dir(dir_to_shred, num_times=1, contents_only=True):
    files_to_shred = os.listdir(dir_to_shred)
    if os.path.isdir(dir_to_shred):
        file_procs = []
        for file in files_to_shred:
            shred_cmd = 'shred -u -n %s %s' % (str(num_times), os.path.join(dir_to_shred, file))
            file_procs.append(subprocess.Popen(shred_cmd, shell=True, stdout=subprocess.PIPE))

        for proc in file_procs:
            proc.wait()
        if not contents_only:
            os.rmdir(dir_to_shred)
    else:
        sys.exit('%s is not a directory' % dir_to_shred)

def copy_dir_contents(the_dir):
    pass

def md5_file(in_path, out_path):
    blocksize = 65536
    in_file = open(in_path, 'rb')
    buf = in_file.read(blocksize)
    hasher = hashlib.md5()

    while len(buf) > 0:
        hasher.update(buf)
        buf = in_file.read(blocksize)
    in_file.close()

    out_file = open(out_path, 'w+')
    out_file.write('%s\t%s\n' % (hasher.digest(), os.path.basename(in_path)))
    out_file.close()

def print_version():
    print '\nadminutils.py\t\tv%s\n' % __VERSION

def get_usage(args):
    usage = ''
    for k in args:
        if len(k) > 2:
            tabs = '\t'*1
        else:
            tabs = '\t'*2
        usage += '\t' + k + tabs + args[k] + '\n'
    return 'Usage: adminutils.py [flags]\n%s' % (usage)

def main(argv):
    if len(argv) == 0 or argv[0] not in args:
        return get_usage(__VALID_ARGS)
    else:
        do_args = {'-v':print_version, '--version':print_version}
        do_args[argv[0]]()

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
