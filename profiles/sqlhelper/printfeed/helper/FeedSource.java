
package sqlhelper.printfeed.model;

import java.io.Serializable;

public class  FeedSource implements Serializable{
    /**
     *  FeedSource generated by xaled/sqlhelper for database printfeed version 1
     *  https://github.com/xaled/sql-helper.git
     */
    private static final long serialVersionUID = 1L;
    //private variables
    

	private String name;


	private String url;


	private String tags;



        // Empty Constructor
        public FeedSource(){

        }

        // Full Constuctor
        
        public FeedSource(String name,String url,String tags){

         this.name = name;
         this.url = url;
         this.tags = tags;
        }


        // Getters and Setters
        

		// getting name
		public String getName(){
			return this.name;

		}
		// setting name
		public void setName(String name){
			this.name= name;
		}


		// getting url
		public String getUrl(){
			return this.url;

		}
		// setting url
		public void setUrl(String url){
			this.url= url;
		}


		// getting tags
		public String getTags(){
			return this.tags;

		}
		// setting tags
		public void setTags(String tags){
			this.tags= tags;
		}


	}
