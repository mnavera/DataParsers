using ProgressMeter



function main()
	argsnum=length(ARGS)

	if(argsnum != 2)
		println("Cewl: cewl url.com -c -w cewl_wordlist")
		println("Usage: cewl_limitwordcount.jl cewl_wordlist <minimum count>")
		exit()
	end

	filepath = ARGS[1] #full name of password list
	fname = basename(filepath) #name of input file=#
	min_count = ARGS[2]

	out_fname="cewl_count_"*min_count*"_"*fname #filename for output file, then create file
	touch(out_fname)
	
	#open file handles we'll need
	outfile = open(out_fname, "w")

	#Declare progress bar and counter
	prog = ProgressUnknown(1, "Current: ")
	accepted,rejected = 0,0

	#change the minimum count type to int so we can use it
	min_count=parse(Int64,min_count)

	for line in eachline(filepath)
		next!(prog; showvalues = [(:Accepted,accepted), (:Rejected,rejected)]) #current line

		w,c = split(line,", ") #split line to isolate count number from word itself


		if(parse(Int64,c) >= min_count)#if word occurs more times than threshold, write to file
			write(outfile,w*"\n")
			accepted+=1
		else
			rejected+=1#else, do nothing and move on to the next loop
			continue
		end

	end




	finish!(prog; showvalues = [(:Accepted,accepted), (:Rejected,rejected)])
	println("\nOutput File: ",out_fname)

	close(outfile)
end
















main()