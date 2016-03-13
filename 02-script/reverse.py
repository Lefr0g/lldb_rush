import lldb

def reverse(debugger, command, result, internal_dict):
	target = debugger.GetSelectedTarget()
	target_str = str(target)
	target_str_reverse = target_str[::-1]
	print 'FT_' + target_str_reverse


def __lldb_init_module(debugger, internal_dict):
	debugger.HandleCommand('command script add -f reverse.reverse reverse')
