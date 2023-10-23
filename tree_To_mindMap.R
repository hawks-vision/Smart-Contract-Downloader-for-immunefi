
library('mindr')

#dir2(path = getwd(), savefile = TRUE, savefilename = "mindr.mm", output = c("mm",
  #  "txt", "md", "Rmd"), backup = TRUE, dir_files = FALSE)

#'''dir2(path = getwd(), savefile = TRUE, savefilename = "mindr.mm", output = c("mm",
 #   "txt", "md", "Rmd"), backup = TRUE, dir_files = FALSE)```

args = commandArgs(trailingOnly=TRUE) #'/root/RST/blockchain/Projects/perennial'
#dir2mm(input)
dir2mm(args[1], dir_files = FALSE, dir_all = TRUE, dir_excluded = "Meta")

output_txt <- dir2mm(args[1])
output <- tempfile(pattern = "file", tmpdir = getwd(), fileext = ".mm")
writeLines(output_txt, output, useBytes = TRUE)
message("Input:  ", args[1], "\nOutput: ", output)


